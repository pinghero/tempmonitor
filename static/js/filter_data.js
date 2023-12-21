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

    // Fetch filter values (customize this based on your filter input methods)
    var locationFilter = document.getElementById('locationFilter').value;
    var temperatureFilter = document.getElementById('temperatureFilter').value;
    var humidityFilter = document.getElementById('humidityFilter').value;

    // Prepare filter data to send to the Flask backend
    var filterData = {
        location: locationFilter,
        temperature: temperatureFilter,
        humidity: humidityFilter
    };

    // Send filter data to Flask backend
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
