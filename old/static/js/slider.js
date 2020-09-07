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

    step: 24 * 60 * 60 * 1000, // Steps of a week
    start: [timestamp(start_date), timestamp(end_date)], // Timestamps for the initial positions
    connect: [false, true, false]
});


// -------- Slider control --------

var dateValues = [
    document.getElementById('event-start'),
    document.getElementById('event-end')
];

dateSlider.noUiSlider.on('update', function (values, handle) {
    dateValues[handle].innerHTML = formatDate(new Date(+values[handle]));
});

function nth(d) {
    if (d > 3 && d < 21) return 'th';
    switch (d % 10) {
        case 1:
            return "st";
        case 2:
            return "nd";
        case 3:
            return "rd";
        default:
            return "th";
    }
}


// Create a string representation of the date.
function formatDate(date) {
    return date.getDate() + nth(date.getDate()) + " " +
        months[date.getMonth()] + " " +
        date.getFullYear();
}
