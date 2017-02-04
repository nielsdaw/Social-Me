/**
 * Created by nielsdaw on 22/11/2016.
 */

$(document).ready(function () {
    // Instance the tour
    var tour = new Tour({
        name: "social-tour",
        backdrop: true,
        template: "<div class='popover tour'>" +
                    "<div class='arrow'></div>" +
                    "<h3 class='popover-title'></h3>" +
                    "<div class='popover-content'></div>" +
                    "<div class='popover-navigation'>" +
                        "<div class='btn-group'>" +
                            "<button class='btn btn-sm btn-danger' data-role='prev'>« Prev</button>" +
                            "<button class='btn btn-sm btn-warning' data-role='next'>Next »</button>"+
                        "</div>"+
                        "<button class='btn btn-sm btn-success' data-role='end'>Close</button>" +
                    "</div>" +
                "</div>",
        steps: [
            {
            element: "#connect-profiles",
            title: "Connect profiles ",
            content: "Here you can connect your social media profiles.",
            placement: "top"
            },
            {
            element: "#social-me",
            title: "Social Me",
            content: "Here you can view your Social Me, which is based on the information you provide on your connected social media profiles.",
            placement: "top"
            },
            {
            element: "#dashboard",
            title: "Dashboard",
            content: "Here you can have a brief overview of your connected social media profiles.",
            placement: "top"
            },
        ]});

        // Initialize the tour
        tour.init();

        // Start the tour
        tour.start();
});
