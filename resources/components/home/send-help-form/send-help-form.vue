<template>
  <div id="send-help-form">
    <form @submit.prevent>
      <div class="mb-2">
        <input
          required
          placeholder="Friend's Number"
          class="phone_number_input"
          type="tel"
          pattern="^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
          title="Please match any of the formats: +1 000.000.0000, +1 000-000-0000, +1 000 000 0000"
        />
      </div>
      <div>
        <select class="contry_select" name="" id="">
          <option value="">Select their country</option>
          <option v-for="(name, code) in countries" :value="code" :key="code">
            {{ name }}
          </option>
        </select>
      </div>
      <div class="submit_button">
        <button class="submit_btn btn-grad">Send Resources</button>
        <a class="mt-2 d-flex justify-content-end" href="#"
          >How does it work?</a
        >
      </div>
    </form>
  </div>
</template>

<script>
import countries from "./countries.json";
import "./styles.scss";
export default {

  data() {
    return {
      countries: countries,
    };
  },
};
</script>

<style>
</style>