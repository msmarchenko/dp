<template>
    <div id="chart">
        <b-container class="mt-5">
            <b-row>
                
                <b-col cols="8">
                    <h2>Графический результат</h2>
                    <apexchart type=bar :options="chart1.plotOptions" :series="chart1.series" />
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
            this.chart1.series[0].data = this.dataShow.x
            // this.chart1.xaxis.categories = this.dataShow.y
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
                    data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
                },],
                chart: {
                    type: 'bar',
                    height: 350
                },
                plotOptions: {
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