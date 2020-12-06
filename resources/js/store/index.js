import Vue from "vue"
import Vuex from "vuex";
// modules
import global from "./modules/global-module.ts";

Vue.use(Vuex)


export default new Vuex.Store({
    modules: {
        global
    }
})
