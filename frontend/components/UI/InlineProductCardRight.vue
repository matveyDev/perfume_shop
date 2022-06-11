<template>
  <div class="row featurette" data-v-20d0eabf="">
    <div class="col-md-7" data-v-20d0eabf="">
      <h2 class="featurette-heading fw-normal lh-1" data-v-20d0eabf="">
        First featurette heading.
        <span class="text-muted" data-v-20d0eabf="">It’ll blow your mind.</span>
      </h2>
      <p class="lead" data-v-20d0eabf="">
        Some great placeholder content for the first featurette here. Imagine
        some exciting prose here.
      </p>
    </div>
    <div class="col-md-5" data-v-20d0eabf="">
      <img
        class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto image"
        width="500"
        height="500"
        :src="inlineBlock.imageName"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    inlineBlock: Object,
  },
};
</script>

<style scoped>
.image {
  overflow: hidden;
  transition: 0.1s;
  display: block;
  border-radius: 10px;
}
.image:hover {
  transform: scale(1.05);
  cursor: pointer;
}
</style>
