$(function () {
    $("#btn-reg-log").on("click", function () {
        if ($("#btn-reg-log").hasClass('checked')) {
            $(".hidden-registration-form-organizate").css('display', 'none')
            $("#btn-reg-log").removeClass('checked')

        } else {
            $(".hidden-registration-form-organizate").css('display', 'flex')
            $("#btn-reg-log").addClass('checked')
        }
    });
})
window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

