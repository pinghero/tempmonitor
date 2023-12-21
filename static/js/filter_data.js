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
            updateTable(data);
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

function resetFilters() {
    $.ajax({
        url: "/get_original_data",
        type: "GET",
        success: function (data) {
            updateTable(data);
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}

function updateTable(data) {
    var tableBody = $('#myTable tbody');
    tableBody.empty();  // Clear the table body

    $.each(data, function (index, temp) {
        var row = tableBody[0].insertRow();  // Access the raw DOM element using [0]

        // Assuming 'timestamp', 'location', 'temperature', and 'humidity' are keys in your data
        row.insertCell(0).textContent = temp.timestamp;
        row.insertCell(1).textContent = temp.location;
        row.insertCell(2).textContent = temp.temperature;
        row.insertCell(3).textContent = temp.humidity;
    });
}

