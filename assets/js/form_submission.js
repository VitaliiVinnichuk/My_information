$(document).ready(function () {
    $('.loader').hide();
    var options = {
        beforeSend: function () {
            //disable input fields
            $('input').attr('disabled', true);
            $('textarea').attr('disabled', true);
            $('.loader').show();
            $('.notification').remove();
        },  // pre-submit callback
        success: function (response) {
            //enable input fields
            $('input').removeAttr('disabled');
            $('textarea').removeAttr('disabled');
            $('.loader').hide();
            //add form field error
            if (response['success'] == false) {
                var errors = response['errors'];
                var error;
                for (error in errors) {
                    error_field = $("#id_" + error);
                    error_field.after('<span class="text-danger notification">' + errors[error] + '</span>')
                }
            }
        },      // post-submit callback
        type: 'post',
        data: $(this).serialize(),
        dataType: 'json'
    };

    // bind to the form's submit event
    $('#user-info-form').submit(function () {
        $(this).ajaxSubmit(options);
        return false;
    });
});

