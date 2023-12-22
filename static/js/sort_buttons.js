//show/hide filter option buttons
function toggleInput(field) {
    var inputFrom = document.getElementById(field + 'From');
    var inputTo = document.getElementById(field + 'To');
    inputFrom.classList.toggle("show");
    inputTo.classList.toggle("show");
}

function toggleLocationInput() {
    var locationInput = document.getElementById('location');
    locationInput.classList.toggle("show");
}