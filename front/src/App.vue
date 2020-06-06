<template>
  <div id="app">
    <Login  @auth="authed" v-if="!auth"/>
    <Home v-if="auth"  />
  </div>
</template>

<script>
  import Login from './components/Login.vue'
  import Home from './components/Home.vue'

export default {
  name: 'app',
  components: {
    Login,
    Home,
  },
   data: function() {
    return {
      auth: false,
    };
  },
   methods: {
     authed:function(){
       this.auth = true
     }
   }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
