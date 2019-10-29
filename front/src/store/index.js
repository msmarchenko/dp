import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
      dataShow: null
  },
  getters: {
    DATASHOW: state => {
        return state.dataShow;
      },
  },
  mutations: {
    SET_DATASHOW: (state, payload) => {
        state.dataShow = payload;
    },
  },
  actions: {
    SAVE_TODO: async (context, payload) => {        
        context.commit('SET_DATASHOW', payload);
    },
  },
});