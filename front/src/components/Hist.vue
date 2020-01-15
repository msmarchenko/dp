<template>
    <div id="chart">
        <b-container class="mt-5">
            <b-row>
                
                <b-col cols="12">
                    <h2>Best Rezeptur</h2>
                    <apexchart type=bar :options="chart1.plotOptions" :series="chart1.series" />
                </b-col>
                
            </b-row>

            <b-row>

                <b-col cols="12">
                    <h2>Best Material</h2>
                    <apexchart type=bar :options="chart2.plotOptions" :series="chart2.series" />
                </b-col>

            </b-row>


            <b-row>

                <b-col cols="12">
                    <h2>Number of Orders </h2>
                    <apexchart type=bar :options="chart3.plotOptions" :series="chart3.series" />
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

        this.dataShow = this.$store.getters.DATASHOW;
        if(this.dataShow != null)
        {
            this.chart1.series[0].data = []
            this.chart1.series[0].data = this.dataShow.x_rez
            this.chart1.plotOptions.xaxis.categories = this.dataShow.y_rez
            this.chart1.plotOptions.title = {text: 'Yield', style: {fontSize:  '16px', color:  '#263238' },}
            this.chart2.series[0].data = []
            this.chart2.series[0].data = this.dataShow.x_mat
            this.chart2.plotOptions.xaxis.categories = this.dataShow.y_mat
            this.chart2.plotOptions.title = {text: 'Yield', style: {fontSize:  '16px', color:  '#263238' },}
            this.chart3.series[0].data = []
            this.chart3.series[0].data = this.dataShow.x_kd_name
            this.chart3.plotOptions.xaxis.categories = this.dataShow.y_kd
            this.chart3.plotOptions.title = {text: '# Orders', style: {fontSize:  '16px', color:  '#263238' },}
        }
    },
    data() {
        return {
            dataShow: null,
            x:[],
            y:[],
            chart1:
            {

                series: [{
                    name: 'Test',
                    data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
                    label: [4,4,4,4,4,4,4,5,6]
                },],
                chart: {
                    type: 'bar',
                    height: 350
                },
                plotOptions: {
                    xaxis: {
                        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
                    },
                    bar: {
                        horizontal: false,
                        columnWidth: '55%',
                        endingShape: 'rounded'
                    },
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    show: true,
                    width: 2,
                    colors: ['transparent']
                },
                xaxis: {
                    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'asd', 'asd'],
                },
                yaxis: {
                    title: {
                        text: '$ (thousands)'
                    }
                },
                fill: {
                    opacity: 1
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return "$ " + val + " thousands"
                        }
                    }
                }
            },
            chart2:
            {

                series: [{
                    name: 'Test',
                    data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
                    label: [4,4,4,4,4,4,4,5,6]
                },],
                chart: {
                    type: 'bar',
                    height: 350
                },
                plotOptions: {
                    xaxis: {
                        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
                    },
                    bar: {
                        horizontal: false,
                        columnWidth: '55%',
                        endingShape: 'rounded'
                    },
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    show: true,
                    width: 2,
                    colors: ['transparent']
                },
                xaxis: {
                    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'asd', 'asd'],
                },
                yaxis: {
                    title: {
                        text: '$ (thousands)'
                    }
                },
                fill: {
                    opacity: 1
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return "$ " + val + " thousands"
                        }
                    }
                }
            },
            chart3:
            {

                series: [{
                    name: 'Test',
                    data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
                    label: [4,4,4,4,4,4,4,5,6]
                },],
                chart: {
                    type: 'bar',
                    height: 350
                },
                plotOptions: {
                    xaxis: {
                        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
                    },
                    bar: {
                        horizontal: false,
                        columnWidth: '55%',
                        endingShape: 'rounded'
                    },
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    show: true,
                    width: 2,
                    colors: ['transparent']
                },
                xaxis: {
                    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'asd', 'asd'],
                },
                yaxis: {
                    title: {
                        text: '$ (thousands)'
                    }
                },
                fill: {
                    opacity: 1
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return "$ " + val + " thousands"
                        }
                    }
                }
            },
        }
    }
}





</script>