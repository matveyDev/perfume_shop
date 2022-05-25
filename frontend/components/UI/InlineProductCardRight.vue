<template>
  <div class="inline-product row featurette">
    <div class="col-md-7">
      <h2 class="featurette-heading">
        {{ inlineBlock.title }}
      </h2>
      <p class="lead">
        {{ inlineBlock.description }}
      </p>
    </div>
    <div class="col-md-5">
      <img
        class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
        width="535"
        height="500"
        :src="'../source/' + inlineBlock.imageName"
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

<style scoped></style>
