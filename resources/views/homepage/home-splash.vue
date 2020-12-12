<template>
  <div id="home_page">
    <video poster="/static/assets/img/home-bg-poster.jpg" playsinline autoplay muted loop class="home_hero">
      <source
        src="/static/assets/videos/hero_background.mp4"
        type="video/mp4"
      />
    </video>
    <header class="viewport-header container">
        <div class="header-column">
          <h1>Thank you for being a friend!</h1>
          <p>
            Send mental health resources to a friend in need 100% anonymously.
          </p>
        </div>
        <div class="header-column">
          <slot/>
          <send-help-form />
        </div>
    </header>
  </div>
</template>

<script>
import SendHelpForm from "../../components/home/send-help-form/send-help-form.vue";
export default {
  components: {
    SendHelpForm,
  },
  mounted() {
   
  },
};
</script>