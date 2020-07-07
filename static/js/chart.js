$(function () {
    chart3.get_data();
});

var chart3 = {
    get_data: function () {
        $.ajax({
            url: "/data/get_city_count",
            type: "GET",
            dataType: "json",
            success: function (data) {
                chart3.render(data);
            }
        });
    },
    render: function (data) {
        var myChart = echarts.init(document.getElementById('chart3'));

        var option = {
            xAxis: {
                type: 'category',
                data: data.xAxis_data
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: data.series_data,
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(220, 220, 220, 0.8)'
                }
            }]
        };

        myChart.setOption(option);
        window.addEventListener('resize', function () {
            myChart.resize();
        });
    }
};