$(document).ready(function () {
    $("#Submit").on('click',
        function () {
            sendAjaxForm('result_form', 'login-form');
            return false;
        }
    );
});
count = 0

function sendAjaxForm(result_form, ajax_form) {
    $.ajax({
        url: `http://127.0.0.1:8000/personApi/`,
        type: "GET", //метод отправки
        dataType: "json", //формат данных
        processData: false,
        contentType: false,
        data: $('#' + ajax_form).serialize(),
        success: function (response) { //Данные отправлены успешно

        },
        error: function (response) { // Данные не отправлены
            console.log(res)
            swal("Успешно купленно!", response['Error']['msg'], "error");
        }
    });
}
