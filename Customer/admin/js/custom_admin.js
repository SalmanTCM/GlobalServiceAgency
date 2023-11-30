(function($) {
    $(document).ready(function() {
        $('body').on('click', '.export_selected_objects', function(e) {
            e.preventDefault();
            $(this).closest('form').submit();
        });
    });
})(django.jQuery);
