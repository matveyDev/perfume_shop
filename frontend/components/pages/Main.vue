<template>
  <div
    id="carouselExampleInterval"
    class="carousel slide"
    data-bs-ride="carousel"
  >
    <div class="carousel-inner">
      <div class="carousel-item active" data-bs-interval="5000">
        <img src="../source/tom_fords.jpg" class="d-block w-100" height="700" />
      </div>
      <div class="carousel-item">
        <img src="../source/mfks.jpg" class="d-block w-100" height="700" />
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleInterval"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleInterval"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>

  <div class="container middle-body">
    <span class="text-header pb-2">Best Fragrance</span>
    <div class="main__cards">
      <div v-for="product in products">
        <ProductCard :product="product"/>
      </div>
      <div class="border-body">
        <hr class="featurette-divider">
        <InlineProductCardRight :inlineBlock="inlineBlock_1"/>
        <hr class="featurette-divider">
        <InlineProductCardLeft/>
        <hr class="featurette-divider">
        <InlineProductCardRight :inlineBlock="inlineBlock_1"/>
        <hr class="featurette-divider">
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "../UI/ProductCard";
import InlineProductCardRight from "../UI/InlineProductCardRight";
import InlineProductCardLeft from "../UI/InlineProductCardLeft";

export default {
  components: {
    ProductCard,
    InlineProductCardRight,
    InlineProductCardLeft,
  },
  data() {
    return {
      // replace on real data
      products: [
        { id: 1, name: "Tom Ford Biiter Peach" },
        { id: 2, name: "Tom Ford Oud Wood" },
        { id: 3, name: "Tom Ford Tobacco Oud" },
        { id: 4, name: "Tom Ford Black Orchid" },
        { id: 5, name: "Tom Ford Sucker" },
        { id: 6, name: "Tom Ford Sucker" },
        { id: 7, name: "Tom Ford Sucker" },
        { id: 8, name: "Tom Ford Sucker" },
      ],
      inlineBlock_1: {
        imageName: "mfks.jpg",
        title: "Title",
        description: "Any description",
      },
    };
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");

.featurette-divider {
  margin: 75px 0;
}
.middle-body {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.main__cards {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  justify-content: space-between;
}
.text-header {
  margin-top: 25px;
  color: #000;
  font-size: 35px;
  font-family: "Roboto", sans-serif;
}
</style>
