<template>
  <div id="home_page">
    <video playsinline autoplay muted loop class="home_hero">
      <source
        src="/static/assets/videos/hero_background.mp4"
        type="video/mp4"
      />
    </video>
    <header class="viewport-header">
      <send-help-form/>
    </header>
  </div>
</template>

<script >
import SendHelpForm from '../../components/home/send-help-form/send-help-form.vue';
export default {
  components: {
    SendHelpForm
  },
  mounted() {},
};
</script>