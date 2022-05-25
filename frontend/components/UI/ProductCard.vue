<template>
  <div class="main">
    <div class="card text-white">
      <img src="../source/tom_fords.jpg" class="card-img" alt="..." />
      <div class="card-img-overlay">
        <h5 class="card-title">{{ product.name }}</h5>
        <p class="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <p class="card-text">Last updated 3 mins ago</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.main {
  max-width: 320px;
  margin: 5px 0;
}
@media (max-width: 1400px) {
  .main {
    max-width: 500px;
  }
}
@media (max-width: 1200px) {
  .main {
    max-width: 400px;
  }
}
@media (max-width: 992px) {
  .main {
    max-width: 325px;
  }
}
@media (max-width: 770px) {
  .main {
    max-width: 100%;
  }
}
</style>
