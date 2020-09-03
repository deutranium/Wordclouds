var dateSlider = document.getElementById('range');

// -------- Create a list of month names --------
var months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];

// -------- Timestamps --------
function timestamp(str) {
    return new Date(str).getTime();
}

// -------- Setup --------
noUiSlider.create(dateSlider, {
// Create two timestamps to define a range.
    range: {
        min: timestamp(start_date),
        max: timestamp(end_date)
    },

    step: 7* 24 * 60 * 60 * 1000, // Steps of a week
    start: [timestamp(start_date), timestamp(end_date)], // Timestamps for the initial positions
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
