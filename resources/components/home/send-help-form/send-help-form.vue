<template>
  <div id="send-help-form">
    <form @submit.prevent="sendText">
      <div class="mb-2">
        <input
          required
          v-model="message_info.number"
          placeholder="Friend's Number"
          class="phone_number_input"
          type="tel"
          pattern="^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
          title="Please match any of the formats: +1 000.000.0000, +1 000-000-0000, +1 000 000 0000"
        />
      </div>
      <div>
        <select v-model="message_info.lang" class="contry_select" name="" id="">
          <option value="">Select their preferred language</option>
          <option v-for="(name, code) in languages" :value="code" :key="code">
            {{ name }}
          </option>
        </select>
      </div>
      <div class="submit_button">
        <button class="submit_btn btn-grad">Send Resources</button>
      </div>
    </form>
  </div>
</template>

<script>
import languages from "./languages.json";
import axios from "axios";
import "./styles.scss";
export default {
  data() {
    return {
      languages: languages,
      message_info: {
        number: "",
        lang: "EN"
      }
    };
  },
  methods: {
    sendText(){
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios.defaults.xsrfCookieName = "csrftoken"
      axios.post('/api/sendText/', this.message_info)
      .then((res) =>{
        alert(res.data)
      })
    }
  }
};
</script>

<style>
</style>