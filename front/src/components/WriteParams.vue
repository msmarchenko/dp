<template>
    <b-container fluid>
        <b-row>
            <b-col cols="4" offset="4">
              <!-- да простит меня бох за бр -->
                <br>
                <div style='border: 1px solid #ccc;padding-top: 50px;padding-bottom: 50px;'>
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                      <b-form-group id="input-group-1">
                          <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                          <b-form-checkbox value="me">Показатель качества</b-form-checkbox>
                          <b-form-checkbox value="that">Тех. Параметры</b-form-checkbox>
                          </b-form-checkbox-group>
                      </b-form-group>
                      <b-form-group id="input-group-2" class="col-3 offset-2">
                          <calendar 
                          v-model="form.date"
                          :range="true"
                          :lang="'rus'"
                         />
                      </b-form-group>
                      <b-form-group id="input-group-3" label="Используемый алгоритм" label-for="input-3" class="col-10 offset-1">
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
          Param1: '',
          Param2: '',
          algos: 'Linear Reg',
          checked: []
        },
        algos: ['Linear Reg', 'BANANA'],
        show: true
      }
    },
    created: function(){
      this.getParams();
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      getParams(){
        axios.get("http://127.0.0.1:8000/api/parameter/")
        .then(resp=>{
          console.log(resp);
        })
        .catch(error=>{
          console.warn(error);
        })
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.Param1 = ''
        this.form.Param2 = ''
        this.form.Param3 = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>