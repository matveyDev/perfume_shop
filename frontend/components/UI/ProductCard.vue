<template>
  <div class="main">
    <a :href="product.url">
      <div class="card text-white image">
      <img src="../source/tom_fords.jpg" class="card-img"/>
      <div class="card-img-overlay">
        <h5 class="card-title">{{ product.name }}</h5>
      </div>
    </div>
    </a>
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
.image {
  overflow: hidden;
  transition: 0.1s;
  display: block;
}
.image:hover {
  transform: scale(1.05);
  cursor: pointer;
}
.main {
  max-width: 500px;
  margin: 5px 0;
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
