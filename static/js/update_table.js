document.addEventListener("DOMContentLoaded", function () {
    // Fetch data from the Flask route
    fetch('/get_table_data')
        .then(response => response.json())
        .then(data => {
            // Get the table body element
            const tableBody = document.querySelector('#myTable tbody');

            // Loop through the data and add rows to the table
            data.forEach(item => {
                const row = tableBody.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                const cell3 = row.insertCell(2);
                const cell4 = row.insertCell(3);

                cell1.textContent = item.timestamp;
                cell2.textContent = item.loction // assuming you want two decimal places
                cell3.textContent = item.temperature.toFixed(2);    // assuming you want two decimal places
                cell4.textContent = item.humidity.toFixed(2);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
