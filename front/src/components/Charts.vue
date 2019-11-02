<template>
    <div id="chart">
        <b-container class="mt-5">
            <b-row>
                <b-col cols="4" >
                    <b-card-group deck>
                        <b-card border-variant="info" header="Параметры" align="center">
                            <b-card-text>
                                <p>
                                   Технические Параметр: ExtB_Ist_Massedruck                                  
                                </p>
                                <p>
                                    Показатель качества: Stippe_-3000                                 
                                </p>

                            </b-card-text>
                        </b-card>
                    </b-card-group>
                    <b-card-group deck class="mt-5">                        
                        <b-card border-variant="info" header="Информация" align="center">
                            <b-card-text>
                                <p>
                                    Коеф. Лин.Рег.: {{parseFloat(coefc).toFixed(2)}}                                    
                                </p>
                                <p>
                                    Среднеквадратическая ошибка: {{parseFloat(mean_squared_error).toFixed(2)}}                                    
                                </p>
                                <p>
                                    ROC/AUC: {{parseFloat(roc_auc).toFixed(2)}}                                    
                                </p>
                                <p>
                                    Дисперсия: {{parseFloat(variance_score).toFixed(2)}}                                    
                                </p>

                            </b-card-text>
                        </b-card>
                        
                    </b-card-group>
                </b-col>
                <b-col cols="8">
                    <h2>Графический результат</h2>
                    <apexchart type=line :options="chart1.chartOptions" :series="chart1.series" />
                </b-col>
                
            </b-row>
            <b-col cols="8" offset="4">
                <apexchart type=line  :options="chart2.chartOptions" :series="chart2.series" />
            </b-col>
        </b-container>
      
      
    </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: 'Charts',
    components: {
        apexchart: VueApexCharts,
    },
    created(){
        
        this.dataShow = this.$store.getters.DATASHOW;        
        if(this.dataShow != null)
        {
            this.chart1.series[0].data = []
            this.chart1.series[1].data = []
            
            this.chart2.series[0].data = []

            this.coefc = this.dataShow.coefc[0][0];
            this.roc_auc = this.dataShow.roc_auc;
            this.mean_squared_error = this.dataShow.mean_squared_error;
            this.variance_score = this.dataShow.variance_score;
            var app = this;
            Object.values(this.dataShow.y_test).map(function(value, key) {
                // eslint-disable-next-line 
                
                app.chart1.series[1].data.push([new Date(app.dataShow.date[key]),  value[0]])
            });
            Object.values(this.dataShow.y_pred).map(function(value, key) {
                // eslint-disable-next-line 
                // console.log([value[0], app.dataShow.y_test[key][0]])    
                app.chart1.series[0].data.push([new Date(app.dataShow.date[key]), value[0]])
            });
            Object.values(this.dataShow.false_positive_rate).map(function(value, key) {
                // eslint-disable-next-line 
                // console.log([value[0], app.dataShow.y_test[key][0]])    
                app.chart2.series[0].data.push({x:value, y:app.dataShow.true_postitve_rate[key]})
            });
        }   
    },
    data() {
        return {
            dataShow: null,
            coefc: 0.0,
            roc_auc: 0.0,
            mean_squared_error: 0.0,
            variance_score: 0.0,
            chart1: 
            {
                
                series: [
                    {
                        name: 'predicts',
                        type: 'line',
                        data: [{
                                    x: 1,
                                        y: 2.14
                                    }, {
                                        x: 1.2,
                                        y: 2.19
                                    }, {
                                        x: 1.8,
                                        y: 2.43
                                    }, {
                                        x: 2.3,
                                        y: 3.8
                                    }, {
                                        x: 2.6,
                                        y: 4.14
                                    }, {
                                        x: 2.9,
                                        y: 5.4
                                    }, {
                                        x: 3.2,
                                        y: 5.8
                                    }, {
                                        x: 3.8,
                                        y: 6.04
                                    }, {
                                        x: 4.55,
                                        y: 6.77
                                    }, {
                                        x: 4.9,
                                        y: 8.1
                                    }, {
                                        x: 5.1,
                                        y: 9.4
                                    }, {
                                        x: 7.1,
                                        y: 7.14
                                    }, {
                                        x: 9.18,
                                        y: 8.4
                                    }]
                    }
                    , 
                    {
                        name: 'real',
                        type: 'line',
                        data: [{
                                    x: 1,
                                    y: 2
                                }, {
                                    x: 2,
                                    y: 3
                                }, {
                                    x: 3,
                                    y: 4
                                }, {
                                    x: 4,
                                    y: 5
                                }, {
                                    x: 5,
                                    y: 6
                                }, {
                                    x: 6,
                                    y: 7
                                }, {
                                    x: 7,
                                    y: 8
                                }, {
                                    x: 8,
                                    y: 9
                                }, {
                                    x: 9,
                                    y: 10
                                }, {
                                    x: 10,
                                    y: 11
                                }]
                    },
                    // {
                    //     name: 'real',
                    //     type: 'line',
                    //     data: [{
                    //                 x: 1,
                    //                 y: 2
                    //             }, {
                    //                 x: 2,
                    //                 y: 3
                    //             }, {
                    //                 x: 3,
                    //                 y: 4
                    //             }, {
                    //                 x: 4,
                    //                 y: 5
                    //             }, {
                    //                 x: 5,
                    //                 y: 6
                    //             }, {
                    //                 x: 6,
                    //                 y: 7
                    //             }, {
                    //                 x: 7,
                    //                 y: 8
                    //             }, {
                    //                 x: 8,
                    //                 y: 10
                    //             }, {
                    //                 x: 9,
                    //                 y: 12
                    //             }, {
                    //                 x: 10,
                    //                 y: 14
                    //             }]
                    // }
                ],
                
                chartOptions: {
                    grid: {
                        row: {
                            colors: ['#e5e5e5', 'transparent'],
                            opacity: 0.5
                        }, 
                        column: {
                            colors: ['#f8f8f8', 'transparent'],
                        }, 
                        xaxis: {
                            lines: {
                            show: true
                            }
                        }
                    },
                    title: {
                        text: 'Линейная регрессия',
                        align: 'center',
                    },
                    dataLabels: {
                        enabled: false
                    },
                    // fill: {
                    //     type: 'solid',
                    // },
                    // markers: {
                    //     size: [6, 0]
                    // },
                    tooltip: {
                        shared: false,
                        intersect: true,
                    },
                    legend: {
                        show: true
                    },
                    xaxis: {
                        // type: 'numeric',
                        type: 'datetime',
                        // tickAmount: 12,
                        // labels: {
                        //     formatter: function(val) {
                        //         return parseFloat(val).toFixed(1)
                        //     }
                        // }
                    },
                    yaxis: [
                        {                            
                            axisTicks: {
                                show: true,
                            },
                            axisBorder: {
                                show: true,
                                color: '#008FFB'
                            },
                            labels: {
                                style: {
                                color: '#008FFB',
                                }
                            },
                            title: {
                                text: "Predicts",
                                style: {
                                color: '#008FFB',
                                }
                            },
                            tooltip: {
                                enabled: true
                            },
                            labels: {
                                formatter: function(val) {
                                    return parseFloat(val).toFixed(1)
                                }
                            }
                        },

                        {
                            seriesName: 'real',
                            opposite: true,
                            axisTicks: {
                                show: true,
                            },
                            axisBorder: {
                                show: true,
                                color: '#00E396'
                            },
                            labels: {
                                style: {
                                    color: '#00E396',
                                }
                            },
                            title: {
                                text: "real",
                                style: {
                                    color: '#00E396',
                                }
                            },
                            labels: {
                                formatter: function(val) {
                                    return parseFloat(val).toFixed(1)
                                }
                            }
                        },                        
                    ],
                    tooltip: {
                        fixed: {
                        enabled: true,
                        position: 'topLeft', 
                        },
                    },
                    legend: {
                        horizontalAlign: 'center',
                    }   
                }
            },
            chart2:{
                series: [
                    {
                        name: '',
                        type:"line",
                        data: []
                    }, 
                    {
                        name: '',
                        type:"line",
                        data: [{x:0, y:0},{x:1, y:1}]
                    }
                ],
                chartOptions: {
                    grid: {
                        row: {
                            colors: ['#e5e5e5', 'transparent'],
                            opacity: 0.5
                        }, 
                        column: {
                            colors: ['#f8f8f8', 'transparent'],
                        }, 
                        xaxis: {
                            lines: {
                                show: true
                            }
                        }
                    },
                    title: {
                        text: 'Receiver operating characteristic',
                        align: 'center',
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        width: [5, 7, 5],
                        curve: 'straight',
                        dashArray: [0, 8, 5]
                    },               
                    tooltip: {
                        shared: false,
                        intersect: true,
                    },
                    legend: {
                        show: false
                    },
                    xaxis: {
                       
                        type: 'numeric',
                        min: 0,
                        max: 1,
                        tickAmount: 0.2,
                        title: {
                            text: "False Positive Rate",                            
                        },
                        labels: {
                            formatter: function(val) {
                                return parseFloat(val).toFixed(1)
                            }
                        }
                    },
                    
                    yaxis: {
                        min: 0,
                        max: 1.03,
                        title: {
                            text: "True Positive Rate",                            
                        },
                    },
                    tooltip: {
                        fixed: {
                        enabled: false,
                        position: 'topLeft', 
                        },
                    },
                }
            }
        }
    }
}
</script>