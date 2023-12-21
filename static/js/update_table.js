// Function to fetch and update the table data
function fetchDataAndUpdateTable() {
    // Check if filters are applied
    var filtersApplied = areFiltersApplied();

    if (filtersApplied) {
        // Only fetch data and update the table if filters are applied
        $.ajax({
            url: "/update_data",
            type: "POST",
            contentType: "application/json;charset=UTF-8",
            success: function (data) {
                updateTable(data);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    }
}

// Function to check if filters are applied
function areFiltersApplied() {
    // Implement your logic to check if filters are applied
    // For example, check if any filter input values are non-empty
    var tempFrom = $('#tempFrom').val();
    var tempTo = $('#tempTo').val();
    var humidityFrom = $('#humidityFrom').val();
    var humidityTo = $('#humidityTo').val();
    var dateFrom = $('#dateFrom').val();
    var dateTo = $('#dateTo').val();
    var location = $('#location').val();

    return tempFrom || tempTo || humidityFrom || humidityTo || dateFrom || dateTo || location;
}

// Function to clear and update the table with new data
function updateTable(data) {
    var tableBody = $('#tableBody');
    tableBody.empty();  // Clear existing rows

    // Append new rows to the tbody
    data.forEach(function (temp) {
        var row = $('<tr>');
        row.append($('<td>').text(temp.timestamp));
        row.append($('<td>').text(temp.location));
        row.append($('<td>').text(temp.temperature));
        row.append($('<td>').text(temp.humidity));
        tableBody.append(row);
    });
}

// Initial data load when the page is loaded
$(document).ready(function () {
    // Load initial data when the page is loaded
    updateTable(JSON.parse('{{ json_data | safe }}'));
});

// Function to apply filters
function applyFilters() {
    fetchDataAndUpdateTable();
}

// Function to reset filters
function resetFilters() {
    // Implement reset filters logic as needed
    fetchDataAndUpdateTable();  // Fetch data without filters when resetting
}
