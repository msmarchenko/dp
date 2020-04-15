import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
      dataShow: null,
      token: null,
  },
  getters: {
    DATASHOW: state => {
      return state.dataShow;
    },
    TOKEN: state => {
      return state.token;
    },
  },
  mutations: {
    SET_DATASHOW: (state, payload) => {
        state.dataShow = payload;
    },
    SET_TOKEN: (state, payload) => {
        state.token = payload;
    },
  },
  actions: {
    SAVE_TODO: (context, payload) => {        
        context.commit('SET_DATASHOW', payload);
    },
    AUTH:(context, payload) => {        
      context.commit('SET_TOKEN', payload);
    },
  },
});