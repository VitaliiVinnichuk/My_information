function initDateFields() {
    $('.datepicker').datepicker({
        dateFormat: 'yy-mm-dd',
        changeYear: true,
        changeMonth: true,
    }).on('dp.hide', function (event) {
        $(this).blur();
    });
}

$(document).ready(initDateFields());