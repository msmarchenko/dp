<template>
    <div id="chart">
        <b-container>
            <b-row>
                <b-col>
                    <apexchart type=scatter   :options="chart1.chartOptions" :series="chart1.series" />
                </b-col>
                <b-col>
                    <apexchart type=bar  :options="chart2.chartOptions" :series="chart2.series" />
                </b-col>
            </b-row>
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
        
        this.dataShow = JSON.parse(this.$store.getters.DATASHOW);        
        if(this.dataShow != null)
        {
            this.chart1.series[0].data = []
            var app = this;
            Object.values(this.dataShow.X_test).map(function(value, key) {
                app.chart1.series[0].data.push([value[0], app.dataShow.y_test[key][0]])
            });
        }
        console.l
    },
    data() {
        return {
            dataShow: null,
            chart1: 
            {
                series: [
                    {
                    name: 'series1',
                    data: [100, 0, -100, 100, -100, 0, 100]
                    }, 
                    // {
                    //     name: 'series2',
                    //     data: [11, 32, 45, 32, 34, 52, 41]
                    // }
                ],
                chartOptions: {
                    chart: {
                        zoom: {
                        enabled: true,
                        type: 'xy'
                        }
                    },
                    xaxis: {
                        tickAmount: 10,
                        labels: {
                            formatter: function(val) {
                                return parseFloat(val).toFixed(1)
                            }
                        }
                    },
                    yaxis: {
                        tickAmount: 7
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