jQuery(function ($) {
    'use strict';
    // -------------------------------------------------------------
    // Countdown
    // -------------------------------------------------------------
    (function () {

        $("#back-countdiown").countdown({
            date: "30 august 2025 12:00:00",
            format: "on"
        });

    }());

}); // JQuery end


$(document).on('click', '.m-menu .dropdown-menu', function (e) {
    e.stopPropagation()
})