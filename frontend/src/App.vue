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
li {
  list-style-type: none;
}
ul {
  margin-left: 0;
  padding-left: 0;
}
body {
  background: rgb(238, 238, 238);
}
</style>
