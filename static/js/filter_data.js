function applyFilters() {
    var tempFrom = parseFloat(document.getElementById('tempFrom').value);
    var tempTo = parseFloat(document.getElementById('tempTo').value);
    var humidityFrom = parseFloat(document.getElementById('humidityFrom').value);
    var humidityTo = parseFloat(document.getElementById('humidityTo').value);
    var dateFrom = parseFloat(document.getElementById('dateFrom').value);
    var dateTo = parseFloat(document.getElementById('dateTo').value);
    var location = parseFloat(document.getElementById('location').value);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/update_data", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Update the table with the received data
            var newData = JSON.parse(xhr.responseText);
            updateTable(newData);
        }
    };

    xhr.send(JSON.stringify({
        tempFrom: tempFrom,
        tempTo: tempTo,
        humidityFrom: humidityFrom,
        humidityTo: humidityTo,
        dateFrom: dateFrom,
        dateTo: dateTo,
        location: location
    }));
}

function resetFilters() {
var xhr = new XMLHttpRequest();
xhr.open("GET", "/get_original_data", true);

xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
        // Update the table with the received original data
        var originalData = JSON.parse(xhr.responseText);
        updateTable(originalData);
    }
};

xhr.send();
}

function updateTable(data) {
    var tableBody = document.querySelector('#myTable tbody');
    tableBody.innerHTML = '';

    data.forEach(function (temp) {
        var row = tableBody.insertRow();
        row.insertCell(0).textContent = temp.timestamp;
        row.insertCell(1).textContent = temp.location;
        row.insertCell(2).textContent = temp.temperature;
        row.insertCell(3).textContent = temp.humidity;
    });
}
