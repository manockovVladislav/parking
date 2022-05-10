function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// function makePasswordRegExp(pass) {
//     var re = /(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9!@#$%^&*a-zA-Z]{5,}/g;
//     return re.test(pass);
// }

$('.regisrtButton').click(function () {
  
    requestCreatePerson();
});

function requestCreatePerson() {

    const csrftoken = getCookie('csrftoken');

    var numberCar = $('#InputNumberCar').val();
    var fio = $('#fio').val();
    var inputPassword = $('#exampleInputPassword1').val();
    var inputPassword2 = $('#exampleInputPassword2').val();

    if (numberCar == '') {
        return alert("Поле номер машины не может быть пустым!");
    }
    if (fio == '') {
        return alert("Поле ФИО не может быть пустым!");
    }

    if (inputPassword == '') {
        return alert("Поле Password не может быть пустым!");
    }
        
    if (inputPassword2 == '') {
        return alert("Поле Password не может быть пустым!");
    }
    if (inputPassword != inputPassword2) {
        return alert("Поля Password не совпадают!");
    }


    var cloneLogin = {
        csrfmiddlewaretoken: csrftoken,
        personLogin: numberCar,
    }


    async function requestCheck(cloneLogin) {

        var flag = $.ajax({
            method: "POST",
            dataType: "json",
            //async: false,
            data: cloneLogin,
            url: 'http://127.0.0.1:8000/registrCheckClone/',
            // headers: { "X-CSRFToken": csrftoken },
            success: function (response) {
                console.log(response);
                if (response.status == "success") {
                    console.log("Success.")
                    return true
                }
                if (response.status == "error") {
                    console.log('есть пользователь');
                    return alert('Такой пользователь существует!')
                }
            },
            error: function (err) {
                console.log("error");
                console.log(err);
                return false
            }
        });

        return flag
    }

    async function requestRegistr(cloneLogin) {
        var flag = await requestCheck(cloneLogin);

        if (flag.status == "success") {

            var dataRegistr = {
                csrfmiddlewaretoken: csrftoken,
                login: numberCar,
                password: inputPassword,
                number: numberCar,
                fioPerson: fio,
            }

            $.ajax({
                method: "POST",
                dataType: "json",
                //async: false,
                data: dataRegistr,
                url: 'http://127.0.0.1:8000/registrPerson/',
                // headers: { "X-CSRFToken": csrftoken },
                success: function (response) {
                    // console.log("success" + JSON.stringify(response)); 
                    console.log(response.status);
                    if (response.status == "success") {
                        $('.registrationsToggle').css('display', 'none');
                    }
                },
                error: function (err) {
                    console.log("error");
                    console.log(err);
                }
            });
        }

    }
    requestRegistr(cloneLogin);
}


$('.enterTalon').click(function () {
    enterSite();
});

function enterSite() {
    const csrftoken = getCookie('csrftoken');
    var numberCarUser = $('#enterNumberCar').val();


    var dataEnter = {
        csrfmiddlewaretoken: csrftoken,
        numberCarUser: numberCarUser,

    }

    $.ajax({
        method: "POST",
        dataType: "json",
        data: dataEnter,
        url: 'http://127.0.0.1:8000/enterSite/',
        // headers: { "X-CSRFToken": csrftoken },
        success: function (response) {
            console.log(response.status);
            if (response.status == "success") {
                window.location.href = 'http://127.0.0.1:8000/statusParking/getParkingNumber/' + response.slug_id;
            }
            
            if(response.status == "car_parking_now"){
                alert('Ваша машина уже на парковке!')
            }

        },
        error: function (err) {
            console.log("error");
            console.log(err);
        }
    });
}


$( "#toggleButton" ).click(function() {
    $( ".registrationsToggle" ).slideToggle( "fast" );
  });
