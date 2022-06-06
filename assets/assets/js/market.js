$(document).ready(function () {
    $("#1").on('click',
        function () {
            sendAjaxForm('result_form', 'form', Number($("#1").prop('id')));
            return false;
        }
    );
    $("#2").on('click',
        function () {
            sendAjaxForm('result_form', 'form', Number($("#2").prop('id')));
            return false;
        }
    );
    $("#3").on('click',
        function () {
            sendAjaxForm('result_form', 'form', Number($("#3").prop('id')));
            return false;
        }
    );
    $("#btn-accept-buy").on('click',
        function () {
            sendBuyForm('result_form', 'form-buy')
            return false;
        }
    );
});
count = 0

function sendAjaxForm(result_form, ajax_form, id) {
    document.getElementById('name-product').textContent = '';
    document.getElementById('type-product').textContent = '';
    document.getElementById('summary-box').textContent = '';

    $.ajax({
        url: `http://127.0.0.1:8000/marketplace/${id}`,
        type: "GET", //метод отправки
        dataType: "json", //формат данных
        processData: false,
        contentType: false, // Сеарилизуем объект
        success: function (response) { //Данные отправлены успешно
            count++
            document.getElementById('name-product').textContent = `Название товара:${response['product'][0]['name']}`;
            document.getElementById('type-product').textContent = `Тип: ${response['product'][0]['type']}`;
            document.getElementById('count-box').textContent = `Количество: ${count}`;
            document.getElementById('summary-box').value = check_sum(
                response['product'][0]['price']
            )

            $('#form-buy').css('display', 'block')
        },
        error: function (response) { // Данные не отправлены
            $('.buy-box').html('Ошибка. Данные не отправлены.');
        }
    });
}

function sendBuyForm(result_form, ajax_form) {
    $.ajax({
        url: `http://127.0.0.1:8000/marketplace/buy/${document.getElementById('summary-box').value}`,
        type: "GET", //метод отправки
        dataType: "json", //формат данных
        processData: false,
        contentType: false, // Сеарилизуем объект
        success: function (response) { //Данные отправлены успешно
            console.log(1)
            swal("Успешно купленно!", "Покупка совершена успешно", "success");
        },
        error: function (response) { // Данные не отправлены
            console.log(response)
            swal(response['errMsg']['status'] + response['errMsg']['msg'] + response['errMsg']['reason'], "Вы можете попробовать еще раз!", "error");
        }
    });
}

old_sum = 0

function check_sum(req_sum) {
    if (old_sum === undefined) {
        old_sum = 0
    }
    result = Number(old_sum) + Number(req_sum)
    console.log(
        (result),
        (Number(old_sum)),
        (Number(req_sum))
    )
    old_sum += Number(req_sum)
    return result
}