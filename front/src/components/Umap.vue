<template>
  <div id="chart">
    <b-container class="mt-5">
      <b-row>
        <b-col>
          <b-card-group deck>
            <b-card border-variant="info" header="Настройка мета параметров" align="center">
              <b-card-text>
                <b-row>
                  <b-col cols="3">
                    <label for="meta.alpha">alpha Lasso</label>
                    <b-form-input
                      id="meta.alpha"
                      name="meta.alpha"
                      v-validate="'required|decimal:3'"
                      v-model="metaParams.alpha"
                      placeholder="Enter alpha"
                    ></b-form-input>
                    <span>{{ errors.first('meta.alpha') }}</span>
                  </b-col>
                  <b-col cols="3">
                    <label for="meta.n_neighbors">n_neighbors UMAP</label>
                    <b-form-input
                      id="meta.n_neighbors"
                      name="meta.n_neighbors"
                      v-validate="'required|decimal:3'"
                      v-model="metaParams.n_neighbors"
                      placeholder="Enter n_neighbors"
                    ></b-form-input>
                    <span>{{ errors.first('meta.n_neighbors') }}</span>
                  </b-col>
                  <b-col cols="3">
                    <label for="meta.min_dist">min_dist UMAP</label>
                    <b-form-input
                      id="meta.min_dist"
                      name="meta.min_dist"
                      v-validate="'required|decimal:3'"
                      v-model="metaParams.min_dist"
                      placeholder="Enter min_dist"
                    ></b-form-input>
                    <span>{{ errors.first('meta.min_dist') }}</span>
                  </b-col>
                  <b-col cols="3">
                    <label for="meta.treshold">treshold</label>
                    <b-form-input
                      id="meta.treshold"
                      name="meta.treshold"
                      v-validate="'required|decimal:3'"
                      v-model="metaParams.treshold"
                      placeholder="Enter treshold"
                    ></b-form-input>
                    <span>{{ errors.first('meta.treshold') }}</span>
                  </b-col>
                </b-row>
                <b-row class="mt-5">
                  <b-col>
                    <b-button
                      variant="primary"
                      v-if="!loading"
                      :disabled="!isFormValid"
                      @click="recalc()"
                    >Рассчитать</b-button>

                    <b-button variant="primary" v-if="loading" disabled>
                      <b-spinner small type="grow"></b-spinner>Идет расчет...
                    </b-button>
                  </b-col>
                </b-row>
              </b-card-text>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>

      <b-row class="mt-5">
        <b-col cols="4">
          <b-card-group deck>
            <b-card border-variant="info" header="Параметры" align="center">
              <b-card-text>
                <p>Параметры которые влияют на показатель качества:</p>
                <ul>
                  <li v-for="val in dataShow.top_parametr_lasso">{{val}}</li>
                </ul>
                <!-- <p>
                                    Показатель качества: Stippe_-3000                                 
                </p>-->
              </b-card-text>
            </b-card>
          </b-card-group>
        </b-col>
        <b-col cols="8">
          <h2>Графический результат</h2>
          <apexchart v-if="!loading" type="scatter" :options="chart1.chartOptions" :series="chart1.series" />
        </b-col>
      </b-row>

      <b-col cols="8" offset="4">
        <!-- <apexchart type=line  :options="chart2.chartOptions" :series="chart2.series" /> -->
      </b-col>
    </b-container>
  </div>
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
    this.render();
  },
  data() {
    return {
      loading: false,
      metaParams: {
        alpha: 2,
        n_neighbors: 100,
        min_dist: 0.05,
        treshold: 47.5
      },
      dataShow: null,
      coefc: 0.0,
      roc_auc: 0.0,
      mean_squared_error: 0.0,
      variance_score: 0.0,
      chart1: {
        series: [
          {
            name: "Черные точки",
            data: [
              [16.4, 5.4],
              [21.7, 2],
              [25.4, 3],
              [19, 2],
              [10.9, 1],
              [13.6, 3.2],
              [10.9, 7.4],
              [10.9, 0],
              [10.9, 8.2],
              [16.4, 0],
              [16.4, 1.8],
              [13.6, 0.3],
              [13.6, 0],
              [29.9, 0],
              [27.1, 2.3],
              [16.4, 0],
              [13.6, 3.7],
              [10.9, 5.2],
              [16.4, 6.5],
              [10.9, 0],
              [24.5, 7.1],
              [10.9, 0],
              [8.1, 4.7],
              [19, 0],
              [21.7, 1.8],
              [27.1, 0],
              [24.5, 0],
              [27.1, 0],
              [29.9, 1.5],
              [27.1, 0.8],
              [22.1, 2]
            ]
          },
          {
            name: "Без дефектов",
            data: [
              [36.4, 13.4],
              [1.7, 11],
              [5.4, 8],
              [9, 17],
              [1.9, 4],
              [3.6, 12.2],
              [1.9, 14.4],
              [1.9, 9],
              [1.9, 13.2],
              [1.4, 7],
              [6.4, 8.8],
              [3.6, 4.3],
              [1.6, 10],
              [9.9, 2],
              [7.1, 15],
              [1.4, 0],
              [3.6, 13.7],
              [1.9, 15.2],
              [6.4, 16.5],
              [0.9, 10],
              [4.5, 17.1],
              [10.9, 10],
              [0.1, 14.7],
              [9, 10],
              [12.7, 11.8],
              [2.1, 10],
              [2.5, 10],
              [27.1, 10],
              [2.9, 11.5],
              [7.1, 10.8],
              [2.1, 12]
            ]
          }
        ],

        chartOptions: {
          grid: {
            row: {
              colors: ["#e5e5e5", "transparent"],
              opacity: 0.5
            },
            column: {
              colors: ["#f8f8f8", "transparent"]
            },
            xaxis: {
              lines: {
                show: true
              }
            }
          },
          title: {
            text: "Уменьшение размерности до 2D",
            align: "center"
          },
          dataLabels: {
            enabled: false
          },
          tooltip: {
            shared: false,
            intersect: true,
            fixed: {
              enabled: true,
              position: "topLeft"
            }
          },
          legend: {
            show: true,
            horizontalAlign: "center"
          },
          xaxis: {
              title: {
                text: "z1 = f(x1,...xn)"
              },
              tickAmount: 10,
              labels: {
                formatter: function(val) {
                  return parseFloat(val).toFixed(3)
                }
              }
          },
          yaxis: {
            title: {
                text: "z2= f(x1,....xn)"
            },
            tickAmount: 10,
            labels: {
              formatter: function(val) {
                return parseFloat(val).toFixed(0)
              }
            }
          }
        }
      },
      chart2: {
        series: [
          {
            name: "",
            type: "line",
            data: []
          },
          {
            name: "",
            type: "line",
            data: [
              { x: 0, y: 0 },
              { x: 1, y: 1 }
            ]
          }
        ],
        chartOptions: {
          grid: {
            row: {
              colors: ["#e5e5e5", "transparent"],
              opacity: 0.5
            },
            column: {
              colors: ["#f8f8f8", "transparent"]
            },
            xaxis: {
              lines: {
                show: true
              }
            }
          },
          title: {
            text: "Receiver operating characteristic",
            align: "center"
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            width: [5, 7, 5],
            curve: "straight",
            dashArray: [0, 8, 5]
          },
          legend: {
            show: false
          },
          xaxis: {
            type: "numeric",
            min: 0,
            max: 1,
            tickAmount: 0.2,
            title: {
              text: "False Positive Rate"
            },
            labels: {
              formatter: function(val) {
                return parseFloat(val).toFixed(1);
              }
            }
          },

          yaxis: {
            min: 0,
            max: 1.03,
            title: {
              text: "True Positive Rate"
            }
          },
          tooltip: {
            shared: false,
            intersect: true,
            fixed: {
              enabled: false,
              position: "topLeft"
            }
          }
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
        algos: "Umap",
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
      console.log("render");
      this.dataShow = this.$store.getters.DATASHOW;
      if (this.dataShow != null) {
        this.chart1.series[0].data = [];
        this.chart1.series[1].data = [];

        this.chart2.series[0].data = [];

        var app = this;
        // eslint-disable-next-line
        var black = [];
        Object.values(this.dataShow.basic_umap.black.x).map(function(
          value,
          key
        ) {
          // eslint-disable-next-line
          //   app.chart1.series[1].data.push({
          //     x: value,
          //     y: app.round(app.dataShow.basic_umap.black.y[key])
          //   });

          black.push({
            x: value,
            y: app.round(app.dataShow.basic_umap.black.y[key])
          });
        });
        this.chart1.series[1].data = black;
        this.$set(this.chart1.series[1], 'data', black);

        Object.values(this.dataShow.basic_umap.red.x).map(function(value, key) {
          // eslint-disable-next-line
          app.chart1.series[0].data.push({
            x: value,
            y: app.round(app.dataShow.basic_umap.black.y[key])
          });
        });
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