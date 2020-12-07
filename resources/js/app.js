import Vue from 'vue';
// Vue store
import store from "./store/index.js";



const files = require.context("../views", true, /\.vue$/i);
files.keys().map(key =>{
    Vue.component(
        key.split("/").pop().split(".")[0],
        files(key).default   
    )
})

new Vue({
    store
}).$mount("#app");