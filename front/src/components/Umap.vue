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
                    <apexchart type=scatter :options="chart1.chartOptions" :series="chart1.series" />
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

            
            var app = this;
            // eslint-disable-next-line 
            Object.values(this.dataShow.basic_umap.black.x).map(function(value, key) {
                // eslint-disable-next-line 
                app.chart1.series[1].data.push({x:value, y:app.dataShow.basic_umap.black.y[key]})
            });
            Object.values(this.dataShow.basic_umap.red.x).map(function(value, key) {
                // eslint-disable-next-line 
                app.chart1.series[0].data.push({x:value, y:app.dataShow.basic_umap.black.y[key]})
            });

            // Object.values(this.dataShow.y_pred).map(function(value, key) {
            //     // eslint-disable-next-line 
            //     // console.log([value[0], app.dataShow.y_test[key][0]])    
            //     app.chart1.series[0].data.push([new Date(app.dataShow.date[key]), value[0]])
            // });
            // Object.values(this.dataShow.false_positive_rate).map(function(value, key) {
            //     // eslint-disable-next-line 
            //     // console.log([value[0], app.dataShow.y_test[key][0]])    
            //     app.chart2.series[0].data.push({x:value, y:app.dataShow.true_postitve_rate[key]})
            // });
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
                            name: "black dotted",
                            data: [
                            [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 0], [10.9, 8.2], [16.4, 0], [16.4, 1.8], [13.6, 0.3], [13.6, 0], [29.9, 0], [27.1, 2.3], [16.4, 0], [13.6, 3.7], [10.9, 5.2], [16.4, 6.5], [10.9, 0], [24.5, 7.1], [10.9, 0], [8.1, 4.7], [19, 0], [21.7, 1.8], [27.1, 0], [24.5, 0], [27.1, 0], [29.9, 1.5], [27.1, 0.8], [22.1, 2]]
                        },
                        {
                            name: "Good",
                            data: [
                            [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 9], [1.9, 13.2], [1.4, 7], [6.4, 8.8], [3.6, 4.3], [1.6, 10], [9.9, 2], [7.1, 15], [1.4, 0], [3.6, 13.7], [1.9, 15.2], [6.4, 16.5], [0.9, 10], [4.5, 17.1], [10.9, 10], [0.1, 14.7], [9, 10], [12.7, 11.8], [2.1, 10], [2.5, 10], [27.1, 10], [2.9, 11.5], [7.1, 10.8], [2.1, 12]]
                        },
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
                        text: 'Уменьшение размерности до 2D',
                        align: 'center',
                    },
                    dataLabels: {
                        enabled: false
                    },                   
                    tooltip: {
                        shared: false,
                        intersect: true,
                        fixed: {
                            enabled: true,
                            position: 'topLeft', 
                        },
                    },
                    legend: {
                        show: true,
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
                        shared: false,
                        intersect: true,
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