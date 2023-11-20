(function ($) {
    $(document).ready(function () {
        // Function to show/hide fields based on selected issue type
        function handleIssueTypeChange() {
            var selectedIssueType = $('#id_issue_types').val();
            var penaltyField = $('#id_penalty');
            var refundPriceField = $('#id_refund_price');
            var serviceChargeField = $('#id_service_charge');

            // Hide all fields initially
            penaltyField.parent().hide();
            refundPriceField.parent().hide();
            serviceChargeField.parent().hide();

            // Show fields based on selected issue type
            if (selectedIssueType === 'refund') {
                refundPriceField.parent().show();
            } else if (selectedIssueType === 'reissue') {
                penaltyField.parent().show();
                refundPriceField.parent().show();
                serviceChargeField.parent().show();
            }
        }

        // Attach the function to the change event of the issue_types field
        $('#id_issue_types').change(handleIssueTypeChange);

        // Trigger the function initially to set the initial state
        handleIssueTypeChange();
    });
})(django.jQuery);
