
$('.enterTalon').click(function () {
    payParking();
});

function payParking() {
    var numberTalon = $('#numberTalon').val();


    var dataEnter = {
        numberTalon: numberTalon,

    }

    $.ajax({
        method: "POST",
        dataType: "json",
        data: dataEnter,
        url: 'http://127.0.0.1:8000/leaveTheParking/payParking/',
        // headers: { "X-CSRFToken": csrftoken },
        success: function (response) {
            console.log(response.status);
            if (response.status == "success") {
                var flag = confirm("Стоймость парковки составила " + response.price + " рублей");
                if(flag){
                    setTimeout(endLoop, 5000);
                }
            }

        },
        error: function (err) {
            console.log("error");
            console.log(err);
        }
    });
}


function endLoop() {
    window.location.href = 'http://127.0.0.1:8000/';
  }
  
  