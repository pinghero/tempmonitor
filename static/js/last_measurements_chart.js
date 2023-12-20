
var ctx = document.getElementById('linechart').getContext('2d');
var data_json = {
{
    data_json | safe
}
}
;
var linechart = new Chart(ctx, {
    type: "line",
    data: {
        labels: data_json.labels,
        datasets: data_json.datasets
    },
    options: {
        scales: {
            y: {
                responsive: false
            }
        }
    }
});
