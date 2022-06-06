$(function () {
    $("#check-btn").on("click", function () {
        if ($("#check-btn").hasClass('checked')) {
            $("#hidden-panel").css('display', 'none')
            $("#check-btn").removeClass('checked')
            $("#check-btn").text('Показать подробную информацию')

        } else {
            $("#hidden-panel").css('display', 'block')
            $("#check-btn").addClass('checked')
            $("#check-btn").text('Скрыть подробную информацию')
        }
    });
});

$(function () {
    $("#btn-open-edit-box-1").on("click", function () {
        if ($("#btn-open-edit-box-1").hasClass('checked')) {
            $(".hidden-adding-info-block-1").css('display', 'none')
            $("#btn-open-edit-box-1").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-1").css('display', 'flex')
            $("#btn-open-edit-box-1").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-2").on("click", function () {
        if ($("#btn-open-edit-box-2").hasClass('checked')) {
            $(".hidden-adding-info-block-2").css('display', 'none')
            $("#btn-open-edit-box-2").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-2").css('display', 'flex')
            $("#btn-open-edit-box-2").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-3").on("click", function () {
        if ($("#btn-open-edit-box-3").hasClass('checked')) {
            $(".hidden-adding-info-block-3").css('display', 'none')
            $("#btn-open-edit-box-3").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-3").css('display', 'flex')
            $("#btn-open-edit-box-3").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-4").on("click", function () {
        if ($("#btn-open-edit-box-4").hasClass('checked')) {
            $(".hidden-adding-info-block-4").css('display', 'none')
            $("#btn-open-edit-box-4").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-4").css('display', 'flex')
            $("#btn-open-edit-box-4").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-5").on("click", function () {
        if ($("#btn-open-edit-box-5").hasClass('checked')) {
            $(".hidden-adding-info-block-5").css('display', 'none')
            $("#btn-open-edit-box-5").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-5").css('display', 'flex')
            $("#btn-open-edit-box-5").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-6").on("click", function () {
        if ($("#btn-open-edit-box-6").hasClass('checked')) {
            $(".hidden-adding-info-block-6").css('display', 'none')
            $("#btn-open-edit-box-6").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-6").css('display', 'flex')
            $("#btn-open-edit-box-6").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-7").on("click", function () {
        if ($("#btn-open-edit-box-7").hasClass('checked')) {
            $(".hidden-adding-info-block-7").css('display', 'none')
            $("#btn-open-edit-box-7").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-7").css('display', 'flex')
            $("#btn-open-edit-box-7").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-8").on("click", function () {
        if ($("#btn-open-edit-box-8").hasClass('checked')) {
            $(".hidden-adding-info-block-8").css('display', 'none')
            $("#btn-open-edit-box-8").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-8").css('display', 'flex')
            $("#btn-open-edit-box-8").addClass('checked')
        }
    });
})
$(function () {
    $("#btn-open-edit-box-9").on("click", function () {
        if ($("#btn-open-edit-box-9").hasClass('checked')) {
            $(".hidden-adding-info-block-9").css('display', 'none')
            $("#btn-open-edit-box-9").removeClass('checked')

        } else {
            $(".hidden-adding-info-block-9").css('display', 'flex')
            $("#btn-open-edit-box-9").addClass('checked')
        }
    });
})
$(function () {
    $("#show-req-org").on("click", function () {
        if ($("#show-req-org").hasClass('checked')) {
            $(".table-org").css('display', 'none')
            $("#show-req-org").removeClass('checked')

        } else {
            $(".table-org").css('display', 'flex')
            $("#show-req-org").addClass('checked')
        }
    });
})
$(function () {
    $("#show-req-event").on("click", function () {
        if ($("#show-req-event").hasClass('checked')) {
            $(".table-event").css('display', 'none')
            $("#show-req-event").removeClass('checked')

        } else {
            $(".table-event").css('display', 'flex')
            $("#show-req-event").addClass('checked')
        }
    });
})
$(function () {
    $("#show-add-info-item").on("click", function () {
        if ($("#show-add-info-item").hasClass('checked')) {
            $(".hidding-more-information").css('display', 'none')
            $("#show-add-info-item").removeClass('checked')

        } else {
            $(".hidding-more-information").css('display', 'flex')
            $("#show-add-info-item").addClass('checked')
        }
    });
})
$(function () {
    $(".btn-show-todolist").on("click", function () {
        if ($(".btn-show-todolist").hasClass('checked')) {
            $(".card-body").css('display', 'none')
            $(".card-footer").css('display', 'none')
            $(".btn-show-todolist").removeClass('checked')

        } else {
            $(".card-body").css('display', 'block')
            $(".card-footer").css('display', 'block')
            $(".btn-show-todolist").addClass('checked')
        }
    });
})