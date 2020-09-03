var dateSlider = document.getElementById('range');

// -------- Create a list of month names --------
var months = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
];

// -------- Timestamps --------
function timestamp(str) {
    return new Date(str).getTime();
}


// -------- Setup --------
noUiSlider.create(dateSlider, {
// Create two timestamps to define a range.
    range: {
        min: timestamp('2010'),
        max: timestamp('2016')
    },

// Steps of a week
    step: 7* 24 * 60 * 60 * 1000,

// Two more timestamps indicate the handle starting positions.
    start: [timestamp('2011'), timestamp('2015')],

});


// -------- Slider control --------

var dateValues = [
    document.getElementById('event-start'),
    document.getElementById('event-end')
];

dateSlider.noUiSlider.on('update', function (values, handle) {
    dateValues[handle].innerHTML = formatDate(new Date(+values[handle]));
});


// Create a string representation of the date.
function formatDate(date) {
    return months[date.getMonth()] + " " +
        date.getFullYear();
}



