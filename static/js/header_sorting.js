var sortedColumn = 0; // Default sorting by timestamp
var sortDirection = 'asc'; // Default sort direction

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, switchcount = 0;
    table = document.getElementById("myTable");
    switching = true;

    // If the same column is clicked, toggle the sort direction
    if (sortedColumn === n) {
        sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
        sortDirection = 'asc'; // Reset to ascending if a different column is clicked
    }

    // Reset all arrows and remove sorted class
    document.querySelectorAll('.sortable .sort-indicator').forEach(indicator => indicator.innerHTML = '');
    document.querySelectorAll('.sortable').forEach(th => th.classList.remove('sorted'));

    // Add arrow based on the current direction
    document.querySelector('.sortable:nth-child(' + (n + 1) + ') .sort-indicator').innerHTML = sortDirection === 'asc' ? '▲' : '▼';
    // Add sorted class to the sorted header
    document.querySelector('.sortable:nth-child(' + (n + 1) + ')').classList.add('sorted');

    // Store the current sorted column
    sortedColumn = n;

    // Sorting logic
    var rows = Array.from(table.getElementsByTagName("tr")).slice(1); // Exclude the header row
    rows.sort(function (a, b) {
        var aValue = a.getElementsByTagName("td")[n].textContent.trim();
        var bValue = b.getElementsByTagName("td")[n].textContent.trim();

        if (sortDirection === 'asc') {
            return aValue.localeCompare(bValue);
        } else {
            return bValue.localeCompare(aValue);
        }
    });

    // Reorder rows in the table
    for (var i = 0; i < rows.length; i++) {
        table.appendChild(rows[i]);
    }
}