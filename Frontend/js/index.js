$(document).ready(function () {
    $("#checkoutModal").modal();

    $.get('http://localhost:8000/apis/events?format=json', function (data, status) {
        $("#eventname").html(data[0].name);
        $("#eventabout").html(data[0].about);
        $("#thumbnail").attr("src", "http://localhost:8000"+data[0].image);
        $("#eprice").html(data[0].price);
        $("#amount").attr("value", data[0].price);
        let eid = data[0].pk
        $("#eventid").attr("value", eid);
        if (data[0].req_name == false) {
            $(".modal_name_div").remove()
        }
        if (data[0].req_email == false) {
            $(".modal_email_div").remove()
        }
        if (data[0].req_addr == false) {
            $(".modal_addr_div").remove()
        }
        if (data[0].req_mobile == false) {
            $(".modal_mobile_div").remove()
        }

        $.get('http://localhost:8000/apis/event/'+eid+'?format=json', function (data, status) {
        for (let index = 0; index < data.length; index++) {
            $(".edates").append("<p>"+data[index].date+"</p>");
            let start_time = data[index].start_time.split(":", 2)
            let end_time = data[index].end_time.split(":", 2)
            $(".etimes").append("<p>"+start_time[0]+":"+start_time[1]+" - "+end_time[0]+":"+end_time[1]+"</p>");
        }
    })
    })

    // $.ajax({
    //     type: 'GET',
    //     url: 'http://localhost:8000/apis/events?format=json',
    //     headers: {
    //         'Access-Control-Allow-Origin': 'http://localhost:8000'
    //     },
    //     success: function (data) {
    //         $("#eventname").html(data[0].name);
    //         $("#eventabout").html(data[0].about);
    //         $("#thumbnail").attr("src", "/YesAvail/Websites/EventMSys/Backend/"+data[0].image);
    //         $("#eprice").html(data[0].price);
    //         $("#amount").attr("value", data[0].price);
    //         eid = data[0].pk
    //     }
    // })

    // $.ajax({
    //     type: 'GET',
    //     url: 'http://localhost:8000/apis/event/'+eid+'?format=json',
    //     headers: {
    //         'Access-Control-Allow-Origin': 'http://localhost:8000'
    //     },
    //     success: function (data) {
    //         for (let index = 0; index < data.length; index++) {
    //             $(".edates").append("<p>"+data[index].date+"</p>");
    //             let start_time = data[index].start_time.split(":", 2)
    //             let end_time = data[index].end_time.split(":", 2)
    //             $(".etimes").append("<p>"+start_time[0]+":"+start_time[1]+" - "+end_time[0]+":"+end_time[1]+"</p>");
    //         }
    // }})
})
