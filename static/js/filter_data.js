// Function to clear the table
function clearTable() {
    var table = document.getElementById("myTable");
    var tbody = table.querySelector('tbody');
    tbody.innerHTML = '';
}

// Function to update the table with new data
function updateTable(data) {
    var table = document.getElementById("myTable");
    var tbody = table.querySelector('tbody');

    // Loop through the data and add rows to the table
    data.forEach(item => {
        var row = tbody.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);

        cell1.textContent = item.location;
        cell2.textContent = item.temperature.toFixed(2);
        cell3.textContent = item.humidity.toFixed(2);
        cell4.textContent = item.timestamp;
    });
}

// Function to handle filter changes
function applyFilters() {
    // Clear the table
    clearTable();

    // Fetch filter values
    var tempFrom = document.getElementById('tempFrom').value;
    var tempTo = document.getElementById('tempTo').value;
    var humidityFrom = document.getElementById('humidityFrom').value;
    var humidityTo = document.getElementById('humidityTo').value;
    var dateFrom = document.getElementById('dateFrom').value;
    var dateTo = document.getElementById('dateTo').value;
    var location = document.getElementById('location').value;

    // Create an object to store filled filters
    var filterData = {
        tempFrom,
        tempTo,
        humidityFrom,
        humidityTo,
        dateFrom,
        dateTo,
        location
    };

    // Send filter data to Flask backend only if at least one filter is filled
    if (Object.values(filterData).some(value => value !== '')) {
        fetch('/apply_filters', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(filterData),
        })
        .then(response => response.json())
        .then(newData => {
            // Update the table with the new data
            updateTable(newData);
        })
        .catch(error => console.error('Error applying filters:', error));
    }
}
