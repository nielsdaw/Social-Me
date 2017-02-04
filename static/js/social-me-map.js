/**
 * Created by nielsdaw on 15/11/2016.
 */

// Variables
var mymap = L.map('mapid').setView([40.416775, -3.703790], 2);
var id = "nillernoels.24baa0ml";
var access_token = "pk.eyJ1IjoibmlsbGVybm9lbHMiLCJhIjoiY2l2am50dmFhMDBiNzJ1cGd0bzVsY3VjMSJ9.Hr1EeBRdOpIOTYHxmXtZSA";

$(document).ready(function () {
    createMap(mymap);
    // setAllMarkers(markers);
});


// Loop through optional list of markers
// and bind it to my map
function setAllMarkers(list1, list2, list3, list4){
    list1 = list1 || 0;
    list2 = list2 || 0;
    list3 = list3 || 0;
    list4 = list4 || 0;

    if (list1){
        for (i = 0; i < list1.length; i++) {
            marker = L.marker([list1[i][0], list1[i][1]]).addTo(mymap);
            marker.bindPopup(list1[i][2]);
        }
    }

    if (list2){
        for (i = 0; i < list2.length; i++) {
            marker = L.marker([list2[i][0], list2[i][1]]).addTo(mymap);
            marker.bindPopup(list2[i][2]);
        }
    }

    if (list3){
        for (i = 0; i < list3.length; i++) {
            marker = L.marker([list3[i][0], list3[i][1]]).addTo(mymap);
            marker.bindPopup(list3[i][2]);
        }
    }

    if (list4){
        for (i = 0; i < list4.length; i++) {
            marker = L.marker([list4[i][0], list4[i][1]]).addTo(mymap);
            marker.bindPopup(list4[i][2]);
        }
    }
}

// create the map
function createMap(map){
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + access_token, {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: id,
        accessToken: access_token
    }).addTo(map);
}

// Ask client for current position
function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            alert(position.coords.latitude + ","+ position.coords.longitude);
        })
    }
    else {
        alert("Geolocation is not supported by this browser.");
    }
}