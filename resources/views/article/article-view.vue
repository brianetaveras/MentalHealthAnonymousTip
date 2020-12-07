<template>
  <div class="container" id="articles_page">
      <div v-if="parsed_article" v-html="converted_markdown"></div>
  </div>
</template>

<script>
import showdown from "showdown";
export default {
  props: ["article"],
  mounted() {
    this.parsed_article = JSON.parse(this.article);
  },
  data() {
    return {
      parsed_article: null,
    };
  },
  computed: {
      converted_markdown: function(){
          let converter = new showdown.Converter()
          return converter.makeHtml(this.parsed_article.resource_link)
      }
  }
};
</script>

<style>
</style>