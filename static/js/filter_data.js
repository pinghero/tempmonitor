function applyFilters() {
    // Get filter values
    var tempFrom = parseFloat(document.getElementById('tempFrom').value);
    var tempTo = parseFloat(document.getElementById('tempTo').value);
    var humidityFrom = parseFloat(document.getElementById('humidityFrom').value);
    var humidityTo = parseFloat(document.getElementById('humidityTo').value);
    var dateFrom = document.getElementById('dateFrom').value;
    var dateTo = document.getElementById('dateTo').value;
    var location = document.getElementById('location').value;

    // Filter the data based on user input
    var filteredData = temps.filter(function (temp) {
        var withinTempRange = (isNaN(tempFrom) || temp.temperature >= tempFrom) &&
            (isNaN(tempTo) || temp.temperature <= tempTo);
        var withinHumidityRange = (isNaN(humidityFrom) || temp.humidity >= humidityFrom) &&
            (isNaN(humidityTo) || temp.humidity <= humidityTo);
        var withinDateRange = (!dateFrom || new Date(temp.timestamp) >= new Date(dateFrom)) &&
            (!dateTo || new Date(temp.timestamp) <= new Date(dateTo));
        var matchesLocation = !location || temp.location.toLowerCase().includes(location.toLowerCase());

        return withinTempRange && withinHumidityRange && withinDateRange && matchesLocation;
    });

    // Update the table with filtered data
    updateTable(filteredData);
}

function updateTable(data) {
    // Clear existing table rows
    var tableBody = document.querySelector('#myTable tbody');
    tableBody.innerHTML = '';

    // Append new rows based on filtered data
    data.forEach(function (temp) {
        var row = tableBody.insertRow();
        row.insertCell(0).textContent = temp.timestamp;
        row.insertCell(1).textContent = temp.location;
        row.insertCell(2).textContent = temp.temperature;
        row.insertCell(3).textContent = temp.humidity;
    });
}
