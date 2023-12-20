var sortedColumn = -1; // Store the index of the sorted column
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("myTable");
    switching = true;
    // Set the sorting direction to ascending if not previously sorted
    dir = sortedColumn === n ? (table.getAttribute('data-dir') === 'asc' ? 'desc' : 'asc') : 'asc';

    // Reset all arrows
    document.querySelectorAll('.sortable .sort-indicator').forEach(indicator => indicator.innerHTML = '');

    // Add arrow based on the current direction
    document.querySelector('.sortable:nth-child(' + (n + 1) + ') .sort-indicator').innerHTML = dir === 'asc' ? '▲' : '▼';

    // Store the current sorted column and direction
    sortedColumn = n;
    table.setAttribute('data-dir', dir);

    // Sorting logic
    var rows = Array.from(table.getElementsByTagName("tr")).slice(1); // Exclude the header row
    rows.sort(function (a, b) {
        var aValue = a.getElementsByTagName("td")[n].textContent.trim();
        var bValue = b.getElementsByTagName("td")[n].textContent.trim();

        if (dir === 'asc') {
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