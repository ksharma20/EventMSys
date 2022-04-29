from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Checkout
from events.models import Event
from .paytm import checksum

PYTM_MUID = "XHYfDh55315404107571"
PYTM_MSKEY = "G26P#Bs1rLbQ8af8"
PYTM_WEB =  "WEBSTAGING"
PYTM_INDUSTRY =  "Retail"
PYTM_CWID = "WEB"
PYTM_CAID = "WAP"

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        eid = request.POST.get('eventid')
        mobile = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pincode = request.POST.get('zip')
        price = request.POST.get('amount')

        order = Checkout.objects.create(event=Event.objects.get(pk=eid), name=name, mobile=mobile, email=email, address=address, pin_code=pincode, amount=price )
        order.save()
        
        # initialize JSON String
        if email:
            body = { 
                "MID": PYTM_MUID,
                "ORDER_ID": "ORDRID-"+str(order.pk),
                'CHANNEL_ID': PYTM_CWID,
                'TXN_AMOUNT': price,
                'WEBSITE': PYTM_WEB,
                'CALLBACK_URL': "http://127.0.0.1:8000/payment/checkin/",
                'INDUSTRY_TYPE_ID': PYTM_INDUSTRY,
                'CUST_ID': email,
                }
        elif mobile:
                body = { 
                "MID": PYTM_MUID,
                "ORDER_ID": "ORDRID-"+str(order.pk),
                'CHANNEL_ID': PYTM_CWID,
                'TXN_AMOUNT': price,
                'WEBSITE': PYTM_WEB,
                'CALLBACK_URL': "http://127.0.0.1:8000/payment/checkin/",
                'INDUSTRY_TYPE_ID': PYTM_INDUSTRY,
                'CUST_ID': str(mobile),
                }
        else:
                body = { 
                "MID": PYTM_MUID,
                "ORDER_ID": "ORDRID-"+str(order.pk),
                'CHANNEL_ID': PYTM_CWID,
                'TXN_AMOUNT': price,
                'WEBSITE': PYTM_WEB,
                'CALLBACK_URL': "http://127.0.0.1:8000/payment/checkin/",
                'INDUSTRY_TYPE_ID': PYTM_INDUSTRY,
                'CUST_ID': "GuestUser_NOEmail_NOMobile",
                }


        # Generate checksum by parameters we have
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys

        paytmChecksum = checksum.generateSignature(body, PYTM_MSKEY)

        body["CHECKSUMHASH"] = paytmChecksum

        print("generateSignature Returns:" + str(paytmChecksum))
        return render(request, 'redirect.html', body)
    
    return redirect('/')

@csrf_exempt
def checkin(request):
    if request.method == 'POST':

        # paytm will send you post request here
        form = request.POST
        body = {}
        for i in form.keys():
            body[i] = form[i]
            #checksum that we need to verify
            if i == 'CHECKSUMHASH':
                paytmChecksum = form[i]
    
        # Verify checksum
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 

        isVerifySignature = checksum.verifySignature(body, PYTM_MSKEY, paytmChecksum)
        print(isVerifySignature)
        if isVerifySignature:
            print("Checksum Matched")
            order = Checkout.objects.last()
            if body["STATUS"] == "TXN_SUCCESS":
                order.paid = True
                order.save()
        else:
            print(request.POST)
    
    return redirect('http://localhost:8080/html/')