// Function to fetch and update the table data
function fetchDataAndUpdateTable() {
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
    fetchDataAndUpdateTable();
});

// Function to apply filters (you can implement this as needed)
function applyFilters() {
    fetchDataAndUpdateTable();
}

// Function to reset filters (you can implement this as needed)
function resetFilters() {
    fetchDataAndUpdateTable();
}
