/**
 * Created by nielsdaw on 22/11/2016.
 */

$(document).ready(function () {
    // Instance the tour
    var tour = new Tour({
        name: "passport-tour",
        steps: [
            {
            element: "#passport",
            title: "Digital passport ",
            content: "This is where I will show basic info of the user, based on info from facebook and instagram."
            },
            {
            element: "#work",
            title: "Working experience",
            content: "Here I will show basic info of the user, based on info from LinkedIn and facebook"
            },
            {
            element: "#preferences",
            title: "Preferences",
            content: "Here I will show basic info of the user, based on info from spotify and facebook (places & likes)."
            },
            {
            element: "#social-map",
            title: "Map",
            content: "Here I will show different places the user has been, based on likes, tags and places from facebook & Instagram"
            }
        ]});

        // Initialize the tour
        tour.init();

        // Start the tour
        tour.start();
});
