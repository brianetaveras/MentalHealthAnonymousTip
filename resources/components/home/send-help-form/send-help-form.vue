<template>
  <div id="send-help-form">
    <div>
      <input placeholder="Friend's Number" class="phone_number_input" type="tel" />
    </div>
    <div>
      <select class="contry_select" name="" id="">
        <option value="">Select their country</option>
        <option v-for="(c, v) in countries" :value="v" :key="c">{{ c }}</option>
      </select>
    </div>
    <div class="submit_button">
      <button class="submit_btn btn-grad">Send Resources</button>
    </div>
  </div>
</template>

<script>
import countries from "./countries.json";
import "./styles.scss"
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