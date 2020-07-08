$(function () {
    jobNeeds.get_data();
    jobSalary.get_data();
    coSalary.get_data();
    expNeeds.get_data();
    degreeNeeds.get_data();
    get_TotalNum();
    citySalary.get_data();
    languageNeeds.get_data();


});

var jobNeeds = {
    get_data: function () {
        $.ajax({
            url: "/data/get_jobs_demand",
            type: "GET",
            dataType: "json",
            success: function (data) {
                jobNeeds.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart1'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '4%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: data.xData,
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {
                    type: 'bar',
                    data: data.yData,
                    barWidth: '35%', //柱子宽度
                    // barGap: 1, //柱子之间间距
                    itemStyle: {
                        normal: {
                            color: '#2f89cf',
                            opacity: 1,
                            barBorderRadius: 5,
                        }
                    }
                }

            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }//岗位需求量
};

var jobSalary = {
    get_data: function () {
        $.ajax({
            url: "/data/get_jobs_avgSalary",
            type: "GET",
            dataType: "json",
            success: function (data) {
                jobSalary.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart2'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {type: 'shadow'}
            },
            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '4%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: data.xData,
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {

                    type: 'bar',
                    data: data.yData,
                    barWidth: '35%', //柱子宽度
                    // barGap: 1, //柱子之间间距
                    itemStyle: {
                        normal: {
                            color: '#27d08a',
                            opacity: 1,
                            barBorderRadius: 5,
                        }
                    }
                }

            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }//岗位平均薪资
};

var citySalary = {
    get_data: function () {
        $.ajax({
            url: "/data/get_city_avgSalary",
            type: "GET",
            dataType: "json",
            success: function (data) {
                citySalary.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },

            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '2%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: data.xData,
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [{
                type: 'bar',
                data: data.yData,
                /*数据格式[1233,1323,444,555,] */
                barWidth: '35%', //柱子宽度
                // barGap: 1, //柱子之间间距
                itemStyle: {
                    normal: {
                        color: '#5BF906',
                        opacity: 1,
                        barBorderRadius: 5,
                    }
                }
            }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
};

var coSalary = {
    get_data: function () {
        $.ajax({
            url: "/data/get_company_demand",
            type: "GET",
            dataType: "json",
            success: function (data) {
                coSalary.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },

            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '2%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: data.xData,//公司名
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [{
                type: 'bar',
                data: data.yData,
                /*数据格式[1233,1323,444,555,] */
                barWidth: '35%', //柱子宽度
                // barGap: 1, //柱子之间间距
                itemStyle: {
                    normal: {
                        color: '#2f89cf',
                        opacity: 1,
                        barBorderRadius: 5,
                    }
                }
            }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
};

// function echarts_4() {
//     // 基于准备好的dom，初始化echarts实例
//     var myChart = echarts.init(document.getElementById('echart4'));
//
//     option = {
//         tooltip: {
//             trigger: 'axis',
//             axisPointer: {
//                 lineStyle: {
//                     color: '#dddc6b'
//                 }
//             }
//         },
//         legend: {
//             top: '0%',
//             data: ['安卓', 'IOS'],
//             textStyle: {
//                 color: 'rgba(255,255,255,.5)',
//                 fontSize: '12',
//             }
//         },
//         grid: {
//             left: '10',
//             top: '30',
//             right: '10',
//             bottom: '10',
//             containLabel: true
//         },
//
//         xAxis: [{
//             type: 'category',
//             boundaryGap: false,
//             axisLabel: {
//                 textStyle: {
//                     color: "rgba(255,255,255,.6)",
//                     fontSize: 12,
//                 },
//             },
//             axisLine: {
//                 lineStyle: {
//                     color: 'rgba(255,255,255,.2)'
//                 }
//
//             },
//
//             data: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
//
//         }, {
//
//             axisPointer: {show: false},
//             axisLine: {show: false},
//             position: 'bottom',
//             offset: 20,
//
//
//         }],
//
//         yAxis: [{
//             type: 'value',
//             axisTick: {show: false},
//             axisLine: {
//                 lineStyle: {
//                     color: 'rgba(255,255,255,.1)'
//                 }
//             },
//             axisLabel: {
//                 textStyle: {
//                     color: "rgba(255,255,255,.6)",
//                     fontSize: 12,
//                 },
//             },
//
//             splitLine: {
//                 lineStyle: {
//                     color: 'rgba(255,255,255,.1)'
//                 }
//             }
//         }],
//         series: [
//             {
//                 name: '安卓',
//                 type: 'line',
//                 smooth: true,
//                 symbol: 'circle',
//                 symbolSize: 5,
//                 showSymbol: false,
//                 lineStyle: {
//
//                     normal: {
//                         color: '#0184d5',
//                         width: 2
//                     }
//                 },
//                 areaStyle: {
//                     normal: {
//                         color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
//                             offset: 0,
//                             color: 'rgba(1, 132, 213, 0.4)'
//                         }, {
//                             offset: 0.8,
//                             color: 'rgba(1, 132, 213, 0.1)'
//                         }], false),
//                         shadowColor: 'rgba(0, 0, 0, 0.1)',
//                     }
//                 },
//                 itemStyle: {
//                     normal: {
//                         color: '#0184d5',
//                         borderColor: 'rgba(221, 220, 107, .1)',
//                         borderWidth: 12
//                     }
//                 },
//                 data: [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4]
//
//             },
//             {
//                 name: 'IOS',
//                 type: 'line',
//                 smooth: true,
//                 symbol: 'circle',
//                 symbolSize: 5,
//                 showSymbol: false,
//                 lineStyle: {
//
//                     normal: {
//                         color: '#00d887',
//                         width: 2
//                     }
//                 },
//                 areaStyle: {
//                     normal: {
//                         color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
//                             offset: 0,
//                             color: 'rgba(0, 216, 135, 0.4)'
//                         }, {
//                             offset: 0.8,
//                             color: 'rgba(0, 216, 135, 0.1)'
//                         }], false),
//                         shadowColor: 'rgba(0, 0, 0, 0.1)',
//                     }
//                 },
//                 itemStyle: {
//                     normal: {
//                         color: '#00d887',
//                         borderColor: 'rgba(221, 220, 107, .1)',
//                         borderWidth: 12
//                     }
//                 },
//                 data: [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 1, 4]
//
//             },
//
//         ]
//
//     };
//
//     // 使用刚指定的配置项和数据显示图表。
//     myChart.setOption(option);
//     window.addEventListener("resize", function () {
//         myChart.resize();
//     });
// }

var languageNeeds = {
    get_data: function () {
        $.ajax({
            url: "/data/get_language_proportion",
            type: "GET",
            dataType: "json",
            success: function (data) {
                languageNeeds.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart6'));
        option = {

            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {d}%",
                position: function (p) {   //其中p为当前鼠标的位置
                    return [p[0] + 10, p[1] - 10];
                }
            },
            legend: {

                top: '90%',
                itemWidth: 10,
                itemHeight: 10,
                data: data.xData,
                //['Java', 'PHP', 'Python', 'C/C++', 'GO', 'ruby'],
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [
                {
                    name: '语言需求比例',
                    type: 'pie',
                    center: ['50%', '42%'],
                    radius: ['0', '70%'],
                    color: ['#187EF0', '#3B89D5', '#FFC300',  '#FF9700',  '#06c8ab', '#5BF906', '#06f0ab'],
                    label: {show: false},
                    labelLine: {show: false},
                    data: data.yData
                    /*数据格式
                    * {{value: 1, name: 'JAVA'},
                    *  {value: 3, name: 'Python'},
                    *  {value: 2, name: 'PHP'},
                    *  {value: 2, name: 'C/C++'},
                    *  {value: 1, name: 'GO'},
                    *  {value: 1, name: 'ruby'},
                    * }
                    * */
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }//语言需求比例
};

var degreeNeeds = {
    get_data: function () {
        $.ajax({
            url: "/data/get_education_demand",
            type: "GET",
            dataType: "json",
            success: function (data) {
                degreeNeeds.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('fb1'));
        option = {

            title: [{
                text: '学历要求',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '16'
                }

            }],
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",
                position: function (p) {   //其中p为当前鼠标的位置
                    return [p[0] + 10, p[1] - 10];
                }
            },
            legend: {

                top: '70%',
                itemWidth: 10,
                itemHeight: 10,
                data: data.xData,
                //['大专', '本科', '硕士', '博士', '其他']
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [
                {
                    name: '学历要求',
                    type: 'pie',
                    center: ['50%', '42%'],
                    radius: ['40%', '60%'],
                    color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                    label: {show: false},
                    labelLine: {show: false},
                    data: data.yData
                    /*数据格式
                    * [{value: 1, name: '大专'},
                    *  {value: 4, name: '本科'},
                    *  {value: 2, name: '硕士'},
                    *  {value: 2, name: '博士'},
                    *  {value: 1, name: '其他'},
                    * ]
                    * */
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }//学历要求
};

var expNeeds = {
    get_data: function () {
        $.ajax({
            url: "/data/get_experience_demand",
            type: "GET",
            dataType: "json",
            success: function (data) {
                expNeeds.render(data);
            }
        });
    },

    render: function (data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('fb2'));
        option = {

            title: [{
                text: '工作经验要求',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '16'
                }

            }],
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",
                position: function (p) {   //其中p为当前鼠标的位置
                    return [p[0] + 10, p[1] - 10];
                }
            },
            legend: {

                top: '70%',
                itemWidth: 10,
                itemHeight: 10,
                data: data.xData,
                //['0', '1年经验', '2年经验', '3-4年经验', '5-7年经验', '8-9年经验', '10年以上经验']
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [
                {
                    name: '工作经验要求',
                    type: 'pie',
                    center: ['50%', '42%'],
                    radius: ['40%', '60%'],
                    color: ['#FFC300', '#FFEC00', '#9C6AD6', '#554DD8', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                    label: {show: false},
                    labelLine: {show: false},
                    data: data.yData
                    /*数据格式
                    * [{value: 1, name: '0'},
                    *  {value: 4, name: '1年经验'},
                    *  ...
                    * ]
                    * */
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }//工作经验要求
};

function get_TotalNum() {
    $.ajax({
        url: "/data/get_enitre_avgSalary",
        type: "GET",
        dataType: "json",
        success: function (data) {
            $("#allNeeds").text(data.zData);
            $("#allSalary").text(data.yData+'万/年');
        }
    });
}

// function echarts_33() {
//     // 基于准备好的dom，初始化echarts实例
//     var myChart = echarts.init(document.getElementById('fb3'));
//     option = {
//         title: [{
//             text: '兴趣分布',
//             left: 'center',
//             textStyle: {
//                 color: '#fff',
//                 fontSize: '16'
//             }
//
//         }],
//         tooltip: {
//             trigger: 'item',
//             formatter: "{a} <br/>{b}: {c} ({d}%)",
//             position: function (p) {   //其中p为当前鼠标的位置
//                 return [p[0] + 10, p[1] - 10];
//             }
//         },
//         legend: {
//             top: '70%',
//             itemWidth: 10,
//             itemHeight: 10,
//             data: ['汽车', '旅游', '财经', '教育', '软件', '其他'],
//             textStyle: {
//                 color: 'rgba(255,255,255,.5)',
//                 fontSize: '12',
//             }
//         },
//         series: [
//             {
//                 name: '兴趣分布',
//                 type: 'pie',
//                 center: ['50%', '42%'],
//                 radius: ['40%', '60%'],
//                 color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
//                 label: {show: false},
//                 labelLine: {show: false},
//                 data: [
//                     {value: 2, name: '汽车'},
//                     {value: 3, name: '旅游'},
//                     {value: 1, name: '财经'},
//                     {value: 4, name: '教育'},
//                     {value: 8, name: '软件'},
//                     {value: 1, name: '其他'},
//                 ]
//             }
//         ]
//     };
//
//     // 使用刚指定的配置项和数据显示图表。
//     myChart.setOption(option);
//     window.addEventListener("resize", function () {
//         myChart.resize();
//     });
// }


















