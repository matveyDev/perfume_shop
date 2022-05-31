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

    <div class="container">
      <div class="album">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          <div v-for="product in products" class="col">
            <ProductCard :product="product"/>
          </div>
        </div>
      </div>
      <div class="body-bottom">
        <hr class="hr">
        <InlineProductCardRight :inlineBlock='inlineBlock_1'/>
        <hr class="hr">
        <InlineProductCardLeft :inlineBlock='inlineBlock_2'/>
        <hr class="hr">
        <InlineProductCardRight :inlineBlock='inlineBlock_1'/>
        <hr class="hr">
      </div>
    </div>


</template>

<script>
import InlineProductCardRight from "../UI/InlineProductCardRight";
import InlineProductCardLeft from "../UI/InlineProductCardLeft";
import ProductCard from '../UI/ProductCard.vue';

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
        { id: 9, name: "Tom Ford Sucker" },
      ],
      inlineBlock_1: {
        imageName: require("../source/mfks.jpg"),
        title: "Title",
        description: "Any description",
      },
      inlineBlock_2: {
        imageName: require("../source/tom_fords.jpg"),
        title: "Title",
        description: "Any description",
      },
    };
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");

.hr {
  margin: 75px 0px;
}
.hr:last-child {
  margin-bottom: 25px;
}
</style>
