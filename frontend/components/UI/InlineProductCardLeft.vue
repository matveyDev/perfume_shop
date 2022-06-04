<template>
  <div class="row featurette">
    <div class="col-md-7 order-md-2">
      <h2 class="featurette-heading">
        Oh yeah, it’s that good.
      </h2>
      <p class="lead">
        Another featurette? Of course. More placeholder content here to give you
        an idea of how this layout would work with some actual real-world
        content in place.
      </p>
    </div>
    <div class="col-md-5 order-md-1">
      <img
        class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
        width="500"
        height="500"
        :src='inlineBlock.imageName'
      />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    inlineBlock: Object
  }
};
</script>

<style scoped>
</style>
