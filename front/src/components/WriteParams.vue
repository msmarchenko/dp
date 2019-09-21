<template>
    <b-container fluid>
        <b-row>
            <b-col cols="3">
                
                <div>
                    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <b-form-group
                        id="input-group-1"
                        label="Param1"
                        label-for="input-1"
                        description="Введите параметр1"
                    >
                        <b-form-input
                        id="input-1"
                        v-model="form.Param1"
                        type="text"
                        required
                        placeholder="0.5"
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-2" label="Param2:" label-for="input-2">
                        <b-form-input
                        id="input-2"
                        v-model="form.Param2"
                        required
                        placeholder="0.5"
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-3" label="Param3:" label-for="input-3">
                        <b-form-select
                        id="input-3"
                        v-model="form.Param3"
                        :options="foods"
                        required
                        ></b-form-select>
                    </b-form-group>

                    <b-form-group id="input-group-4">
                        <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                        <b-form-checkbox value="me">Check me out</b-form-checkbox>
                        <b-form-checkbox value="that">Check that out</b-form-checkbox>
                        </b-form-checkbox-group>
                    </b-form-group>

                    <b-button type="submit" variant="primary">Submit</b-button>
                    <b-button type="reset" variant="danger">Reset</b-button>
                    </b-form>
                    <!-- <b-card class="mt-3" header="Form Data Result">
                    <pre class="m-0">{{ form }}</pre> -->
                    </b-card>
                </div>

            </b-col>
            <b-col></b-col>
            <b-col></b-col>
        </b-row>
    </b-container>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          Param1: '',
          Param2: '',
          Param3: 'Carrots',
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
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