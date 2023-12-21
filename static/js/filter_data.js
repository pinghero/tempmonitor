function applyFilters() {
    var tempFrom = parseFloat($('#tempFrom').val());
    var tempTo = parseFloat($('#tempTo').val());
    var humidityFrom = parseFloat($('#humidityFrom').val());
    var humidityTo = parseFloat($('#humidityTo').val());
    var dateFrom = parseFloat($('#dateFrom').val());
    var dateTo = parseFloat($('#dateTo').val());
    var location = parseFloat($('#location').val());

    $.ajax({
        url: "/update_data",
        type: "POST",
        contentType: "application/json;charset=UTF-8",
        data: JSON.stringify({
            tempFrom: tempFrom,
            tempTo: tempTo,
            humidityFrom: humidityFrom,
            humidityTo: humidityTo,
            dateFrom: dateFrom,
            dateTo: dateTo,
            location: location
        }),
        success: function (data) {
            clearTable();  // Clear the tbody
            updateTable(data);
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

function clearTable() {
    var tableBody = document.getElementById('myTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';  // Clear all content inside the tbody
}

function updateTable(data) {
    var tableBody = document.getElementById('myTable').getElementsByTagName('tbody')[0];

    // Append new rows to the tbody
    data.forEach(function (temp) {
        var row = document.createElement('tr');
        row.innerHTML = `
            <td>${temp.timestamp}</td>
            <td>${temp.location}</td>
            <td>${temp.temperature}</td>
            <td>${temp.humidity}</td>
        `;
        tableBody.appendChild(row);
    });
}
