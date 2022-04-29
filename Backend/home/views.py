from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<center><h1>No Template Available use this server for apis !!</h1></center>")
