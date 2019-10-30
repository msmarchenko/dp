<template>
    <b-container fluid>
        <b-row>
            <b-col cols="8" offset="2">
              <!-- да простит меня бох за бр -->
                <br>
                <div style='border: 1px solid #ccc;padding-top: 50px;padding-bottom: 50px;'>
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                      <!-- <b-form-group id="input-group-1">
                          <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                            <b-form-checkbox value="me">Показатель качества</b-form-checkbox>
                            <b-form-checkbox value="that">Тех. Параметры</b-form-checkbox>
                          </b-form-checkbox-group>
                      </b-form-group> -->
                      <b-form-group id="input-group-2" class="col-3 offset-4" >
                          <calendar 
                          v-model="form.date"
                          :range="true"
                          :lang="'rus'"
                         />
                      </b-form-group>
                      <b-form-group id="input-group-3" label="Выбор параметров" style="border-top: 1px solid #ccc;">
                        <div v-if="params.Control.length > 0">
                          <b-container>
                            <b-row >
                              <b-col cols="6">
                                Тех. Параметры
                              </b-col>
                              <b-col cols="6">                                
                                Показатель качества
                              </b-col>
                            </b-row>
                            <b-row >
                              <b-col cols="4" offset="1">
                                  <b-form-checkbox-group v-model="form.params.Control" id="checkboxes-4" style="border: 1px solid #ccc;height:200px;word-break: break-all; overflow-y: scroll; overflow-x: hidden;">
                                    <b-form-checkbox v-for="(value, key) in params.Control" :key="key" :value="value.id">{{value.name}}</b-form-checkbox>
                                  </b-form-checkbox-group>
                                  <div class="mt-3">
                                    <b-button variant="primary" @click="addAll('Control')">add all</b-button>
                                    <b-button variant="danger" @click="empty('Control')">add all</b-button>
                                  </div>
                                  
                              </b-col>
                              <b-col cols="4" offset="2" >
                                  <b-form-checkbox-group v-model="form.params.Quality" id="checkboxes-4" style="border: 1px solid #ccc;height:200px;word-break: break-all; overflow-y: scroll; overflow-x: hidden;">
                                    <b-form-checkbox v-for="(value, key) in params.Quality" :key="key" :value="value.id">{{value.name}}</b-form-checkbox>
                                  </b-form-checkbox-group>
                                  <div class="mt-3">
                                    <b-button variant="primary" @click="addAll('Quality')">add all</b-button>
                                    <b-button variant="danger" @click="empty('Quality')">add all</b-button>
                                  </div>
                              </b-col>
                            </b-row>
                          </b-container>
                        </div>
                      </b-form-group>
                      <b-form-group id="input-group-4" label="Используемый алгоритм" label-for="input-3" class="mt-3 col-10 offset-1" style="border-top: 1px solid #ccc;">
                          <b-form-select
                          id="input-3"
                          v-model="form.algos"
                          :options="algos"
                          required
                          ></b-form-select>
                      </b-form-group>

                     
                    <b-button type="submit" variant="primary">Submit</b-button>
                    <!-- <b-button type="reset" variant="danger">Reset</b-button> -->
                    </b-form>
                    <!-- <b-card class="mt-3" header="Form Data Result">
                    <pre class="m-0">{{ form }}Rfr</pre> -->
                    <!-- </b-card> -->
                </div>

            </b-col>
            <b-col></b-col>
            <b-col></b-col>
        </b-row>
    </b-container>
</template>

<script>
  import axios from 'axios';
  import calendar from 'vue-datepicker-ui'
  export default {  
    components: {
      calendar,
    },
    data() {
      return {
        form: {
          date:  [
            new Date(),
            new Date()
          ],
          algos: 'Linear Reg',
          params: {
            Control:[],
            Quality: []
          }
        },
        params: {
          Control:[],
          Quality: []
        },
        algos: ['Linear Reg', 'BANANA'],
        show: true
      }
    },
    created: function(){
      this.getParams();
    },
    methods: {
      empty(type){
        var app = this;
          app.form.params[type] = [];
      },
      addAll(type){
        var app = this;
          app.params[type].forEach(param => {
            app.form.params[type].push(param.id);
          })
          this.$nextTick(() => {
            this.show = true
          })
      },
      onSubmit(evt) {
        evt.preventDefault()
        // eslint-disable-next-line 

        

        
        axios.post("http://127.0.0.1:8000/api/calc/calc/",this.form)
        .then(resp=>{
          // eslint-disable-next-line
          this.$store.dispatch('SAVE_TODO', resp.data);
          
        })
        .catch(error=>{
          // eslint-disable-next-line
          console.warn(error);
        })
        // eslint-disable-next-line
        console.log(JSON.stringify(this.form))
      },
      getParams(){
        var app = this;
        axios.get("http://127.0.0.1:8000/api/parameter/")
        .then(resp=>{
          app.fillParams(resp['data']);
        })
        .catch(error=>{
          // eslint-disable-next-line
          console.warn(error);
        })
      },
      fillParams(sources){
        var app = this;
        sources.forEach(element => {
          app.params[element.position].push(element);
        })
        this.$nextTick(() => {
          this.show = true
        })
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.Param1 = ''
        this.form.Param2 = ''
        this.form.Param3 = null
        // this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>