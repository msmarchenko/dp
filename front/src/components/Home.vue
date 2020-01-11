<template>
    <div>
        <div>
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="#">Интерфейс</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>                

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown text="Lang" right>
                    <b-dropdown-item href="#">EN</b-dropdown-item>                    
                    <b-dropdown-item href="#">RU</b-dropdown-item>
                    </b-nav-item-dropdown>

                    <b-nav-item-dropdown right>
                    <!-- Using 'button-content' slot -->
                    <template v-slot:button-content>
                        <em>User</em>
                    </template>
                    <b-dropdown-item href="#">Profile</b-dropdown-item>
                    <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
        <b-nav tabs>
            <b-nav-item :active="inputsEnable"  @click="ShowInputs">Ввод параметров</b-nav-item>
            <b-nav-item :active="!inputsEnable" @click="ShowGraphs">Графики</b-nav-item>
        </b-nav>
        <div v-if="inputsEnable">
            <WriteParams @calc="calcGood"></WriteParams>
        </div>
         <div v-if="!inputsEnable">
            <!-- <Charts></Charts> -->
            <component :is="componentsChart" v-if="componentsChart"/>
        </div>
    </div>
</template>
<script>
export default {
    components: {
        WriteParams: () => import('./WriteParams.vue'),
        Charts: () => import('./Charts.vue'),
        RandomForest: () => import('./ForestChart.vue'),
    },
    data(){
        
        return{
            inputsEnable: true,
            componentsChart: null,
        }
    },
    methods:{
        calcGood(algos){
            // console.log("Algoritm", algos);
            if(algos == "Random Forest"){
                this.componentsChart = () => import('./ForestChart.vue');
            }else if(algos == "Hist"){                
                this.componentsChart = () => import('./Hist.vue');
            }else{
                this.componentsChart = () => import('./Charts.vue');
            }
            this.inputsEnable = !this.inputsEnable;
        },
        ShowInputs(){
            this.inputsEnable = !this.inputsEnable;
        },
        ShowGraphs() {
            this.inputsEnable = !this.inputsEnable;
            return 1;
        }
    }
}
</script>

