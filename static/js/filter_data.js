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
            clearTable();  // Clear the table before updating
            // Commenting out updateTable to confirm clearing
            // updateTable(data);
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

function clearTable() {
    // Remove all rows except the first one (header)
    $('#myTable tbody tr:not(:first)').remove();
}

function updateTable(data) {
    var tableBody = $('#myTable tbody');

    // // Append new rows to the table
    // $.each(data, function (index, temp) {
    //     var row = $('<tr>');
    //     row.append($('<td>').text(temp.timestamp));
    //     row.append($('<td>').text(temp.location));
    //     row.append($('<td>').text(temp.temperature));
    //     row.append($('<td>').text(temp.humidity));
    //     tableBody.append(row);
    // });
}
