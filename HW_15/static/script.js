
(function(window, document, $) {
        var request = $.ajax({
            url: 'http://127.0.0.1:5000/comment',
            data: form.serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });

        $(document).ready(function() {
        var form = $( "commentForm[name='comment']" );
        var result = $( ".result" );
        form.submit(function(event) {
            sendForm(form, result);
            event.preventDefault();
        });
    });
})(window, document, jQuery);




