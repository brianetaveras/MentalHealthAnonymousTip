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
        <select v-model="message_info.lang" class="contry_select" name id>
          <option value>Select their preferred language</option>
          <option v-for="(name, code) in languages" :value="code" :key="code">{{ name }}</option>
        </select>
      </div>
      <div class="submit_button">
        <button
          :disabled="is_message_sending"
          class="submit_btn btn-grad"
        >{{is_message_sending ? "Sending..." : "Send Resources"}}</button>
      </div>
    </form>
  </div>
</template>

<script>
import languages from "./languages.json";
import axios from "axios";
import toastr from "toastr";
import "./styles.scss";
export default {
  data() {
    return {
      languages: languages,
      message_info: {
        number: "",
        lang: "EN"
      },
      error: null,
      is_message_sending: false
    };
  },
  methods: {
    sendText() {
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      this.is_message_sending = true;
      axios
        .post("/api/sendText/", this.message_info)
        .then(res => {
          toastr.success("Message sent!");
          this.is_message_sending = false;
        })
        .catch(err => {
          this.is_message_sending = false;
          if (err.response.data) {
            toastr.error(err.response.data);
          } else {
            toastr.error("There was a server error. Please try again later.");
          }
        });
    }
  }
};
</script>

<style>
</style>