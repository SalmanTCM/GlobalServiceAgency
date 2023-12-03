// static/admin/js/custom_admin.js
(function($){
    $(document).ready(function(){
        function toggleFieldVisibility() {
            var issueTypeValue = $('#id_issue_types').val();
            var penaltyInput = $('#id_penalty').closest('.form-row');
            var refundInput = $('#id_refund_price').closest('.form-row');
            var serviceChargeInput = $('#id_service_charge').closest('.form-row');

            if (issueTypeValue === 'no_issue') {
                penaltyInput.hide();
                refundInput.hide();
                serviceChargeInput.hide();
            } else if (issueTypeValue === 'refund' || issueTypeValue === 'reissue') {
                penaltyInput.show();
                refundInput.show();
                serviceChargeInput.show();
            } else {
                penaltyInput.hide();
                refundInput.hide();
                serviceChargeInput.hide();
            }
        }

        // Initial toggle on page load
        toggleFieldVisibility();

        // Bind the toggle function to the change event of the issue_types field
        $('#id_issue_types').change(function(){
            toggleFieldVisibility();
        });
    });
})(django.jQuery);
