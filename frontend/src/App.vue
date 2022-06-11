<template>
  <Navbar/>
  <router-view></router-view>
  <Footer/>
</template>

<script>
import Main from "../components/pages/Main";
import Navbar from "../components/static/Navbar";
import Footer from "../components/static/Footer";

export default {
  components: {
    Main,
    Navbar,
    Footer,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");

* {
  font-family: 'Roboto';
}
html, body {
  height: 100%;
}
#app {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}
li {
  list-style-type: none;
}
ul {
  margin-left: 0;
  padding-left: 0;
}
#app {
  background: rgb(238, 238, 238);
}
</style>
