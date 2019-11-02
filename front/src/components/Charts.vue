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
                                    Коеф. Лин.Рег.: {{coefc}}                                    
                                </p>
                                <p>
                                    Cреднеквадратическая ошибка: {{mean_squared_error}}                                    
                                </p>
                                <p>
                                    ROC/AUC: {{roc_auc}}                                    
                                </p>
                                <p>
                                    Дисперсия: {{variance_score}}                                    
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
            <b-col>
                <!-- <apexchart type=bar  :options="chart2.chartOptions" :series="chart2.series" /> -->
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
            this.coefc = this.dataShow.coefc[0][0];
            this.roc_auc = this.dataShow.roc_auc;
            this.mean_squared_error = this.dataShow.mean_squared_error;
            this.variance_score = this.dataShow.variance_score;
            var app = this;
            Object.values(this.dataShow.X_test).map(function(value, key) {
                // eslint-disable-next-line 
                
                app.chart1.series[0].data.push({x:value[0], y:app.dataShow.y_test[key][0]})
            });
            Object.values(this.dataShow.y_pred).map(function(value, key) {
                // eslint-disable-next-line 
                // console.log([value[0], app.dataShow.y_test[key][0]])    
                app.chart1.series[1].data.push({x:app.dataShow.X_test[key][0], y:value[0]})
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
                        name: 'Parametrs',
                        type: 'scatter',
                        data: [{ x: 1,
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
                    }, 
                    {
                        name: 'predict',
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
                                    y: 10
                                }, {
                                    x: 9,
                                    y: 12
                                }, {
                                    x: 10,
                                    y: 14
                                }]
                    }
                ],
                chartOptions: {
                    fill: {
                        type: 'solid',
                    },
                    markers: {
                        size: [6, 0]
                    },
                    tooltip: {
                        shared: false,
                        intersect: true,
                    },
                    legend: {
                        show: true
                    },
                    xaxis: {
                        type: 'numeric',
                        tickAmount: 12,
                        labels: {
                            formatter: function(val) {
                                return parseFloat(val).toFixed(1)
                            }
                        }
                    },
                    yaxis:{
                        labels: {
                            formatter: function(val) {
                                return parseFloat(val).toFixed(1)
                            }
                        }
                    }   
                }
            },
            chart2:{
                series: [{
                name: 'Marine Sprite',
                data: [44, 55, 41, 37, 22, 43, 21]
                }, {
                name: 'Striking Calf',
                data: [53, 32, 33, 52, 13, 43, 32]
                }, {
                name: 'Tank Picture',
                data: [12, 17, 11, 9, 15, 11, 20]
                }, {
                name: 'Bucket Slope',
                data: [9, 7, 5, 8, 6, 9, 4]
                }, {
                name: 'Reborn Kid',
                data: [25, 12, 19, 32, 25, 24, 10]
                }],
                chartOptions: {
                chart: {
                    stacked: true,
                    stackType: '100%'
                },
                plotOptions: {
                    bar: {
                    horizontal: true,
                    },

                },
                stroke: {
                    width: 1,
                    colors: ['#fff']
                },

                title: {
                    text: '100% Stacked Bar'
                },
                xaxis: {
                    categories: [2008, 2009, 2010, 2011, 2012, 2013, 2014],
                },

                tooltip: {
                    y: {
                    formatter: function (val) {
                        return val + "K"
                    }
                    }
                },
                fill: {
                    opacity: 1

                },

                legend: {
                    position: 'top',
                    horizontalAlign: 'left',
                    offsetX: 40
                }
                }
            }
        }
    }
}
</script>