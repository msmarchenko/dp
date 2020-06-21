<template>
  <b-container class="mt-5">
    <b-row>
      <b-card-group deck class="mt-5" cols=4>                        
        <b-card border-variant="info" header="Информация" align="center">
          <b-card-text>
            <p>
                ROC/AUC: {{parseFloat(roc_auc).toFixed(2)}}                                             
            </p>

            <P>True Positive: {{TP}}</P>                     
            <p>False Positive: {{FP}} </p>                               
            <p>True Negative: {{TN}} </p>                               
            <p>False Negative: {{FN}}   </p>
          </b-card-text>
        </b-card>        
      </b-card-group>
      <b-col cols="8">
        <h2>Графический результат</h2>
        <apexchart
          v-if="!loading"
          type="line"
          :options="chart1.chartOptions"
          :series="chart1.series"
        />
        <apexchart type=line  :options="chart2.chartOptions" :series="chart2.series" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
export default {
  name: "Charts",
  components: {
    apexchart: VueApexCharts
  },
  created() {
    // let txt =
    //   '{"cnn":{"false_positive_rate":[0.0,0.1694915254237288,1.0],"true_postitve_rate":[0.0,0.7410714285714286,1.0],"roc_auc":0.7857899515738499,"errors":[83,150,735,29]}}';

    // this.dataShow = JSON.parse(txt);
    this.dataShow = this.$store.getters.DATASHOW;
    this.render();
  },
  data() {
    return {
      loading: false,
      dataShow: null,
      coefc: 0.0,
      roc_auc: 0.0,
      mean_squared_error: 0.0,
      variance_score: 0.0,
      TP: 0,
      FP: 0,
      TN: 0,
      FN: 0,
      chart1: {
        series: [
          {
            name: "Предсказание нейройнной сети",
            data: []
          },
          {
            name: "Истинна",
            data: []
          }
        ],

        chartOptions: {
            chart: {
              height: 350,
              type: 'line',
              zoom: {
                enabled: false
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            title: {
              text: 'Отношение экспериментальных данных с спрогнозированными',
              align: 'left'
            },
            grid: {
              row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
              },
            },
            yaxis:{
              min: 0,
              max: 1,
              title: {
                  text: "Класс",                            
              },
            },
            xaxis: {
              //categories: [],
              type: 'datetime',
              title: {
                  text: "Время",                            
              },
              tickAmount: 10,
              labels: {
                show: true,
                rotate: -45,
                format: 'HH:mm',
                datetimeFormatter: {
                    year: 'yyyy',
                    month: "MMM 'yy",
                    day: 'dd MMM',
                    hour: 'HH:mm',
                },
              },
              axisTicks: {
                  show: true,
                  borderType: 'solid',
                  color: '#78909C',
                  height: 6,
                  offsetX: 0,
                  offsetY: 0
              },
            }
        },
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
                      title: {
                        text: "True Positive Rate"
                      },
                      labels: {
                        formatter: function(val) {
                            return parseFloat(val).toFixed(1)
                        }
                      }
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
    };
  },
  methods: {
    round(value) {
      return parseFloat(value).toFixed(5);
    },
    recalc() {
      this.loading = true;
      let request = {
        algos: "CNN",
        params: this.metaParams
      };
      var app = this;
      axios
        .post("http://127.0.0.1:8000/api/calc/calc/", request)
        .then(resp => {
          this.$store.dispatch("SAVE_TODO", resp.data);
          this.$emit("calc", "Umap");

          this.$nextTick(() => {
            this.render();
            app.loading = false;
          });
        })
        .catch(error => {
          alert("С данными параметрами расчет не возможен");
          // eslint-disable-next-line
          console.warn(error);
          app.loading = false;
        });
    },
    render() {
      // eslint-disable-next-line
      console.log("render", this.dataShow);
    //   this.dataShow = this.$store.getters.DATASHOW;
      if (this.dataShow != null) {
        this.chart1.series[0].data = [];
        this.chart1.series[1].data = [];

        // this.chart2.series[0].data = [];

        var app = this;
        // eslint-disable-next-line
        var black = [];
        // eslint-disable-next-line
        var category = [];
        Object.values(this.dataShow.cnn.date).map(function(value,key) {
          // eslint-disable-next-line
          black.push({y:app.dataShow.cnn.y_orig[key], x: new Date(app.dataShow.cnn.date[key]).getTime()});
        });
        this.chart1.series[1].data = black;
        this.$set(this.chart1.series[1], "data", black);

        Object.values(this.dataShow.cnn.date).map(function(value, key) {
          // eslint-disable-next-line
          app.chart1.series[0].data.push({y:app.dataShow.cnn.y_pred[key], x:value});
        });
        this.roc_auc = this.dataShow.cnn.roc_auc;

        this.TP = this.dataShow.cnn.errors[0];
        this.FP = this.dataShow.cnn.errors[1];
        this.TN = this.dataShow.cnn.errors[2];
        this.FN = this.dataShow.cnn.errors[3];
        Object.values(this.dataShow.cnn.false_positive_rate).map(function(value, key) {
            // eslint-disable-next-line  
            app.chart2.series[0].data.push({x:value, y:app.dataShow.cnn.true_postitve_rate[key]})
        });

        // this.$set(this.chart1.chartOptions.xaxis, "categories", category);
      }
      this.$nextTick();
    }
  },
  computed: {
    isFormValid() {
      return Object.keys(this.fields).every(field => this.fields[field].valid);
    }
  }
};
</script>