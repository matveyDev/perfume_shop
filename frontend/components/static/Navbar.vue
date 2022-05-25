<template>
  <header class="p-3 bg-dark text-white sticky-top">
    <div class="my-navbar container">
      <div class="my-navbar-left">
        <a class="shop-name" href="/">spicyPerfume</a>
        <div class="dropdown">
          <button class="dropdown-btn">Brands</button>
          <div class="dropdown-content">
            <div v-for="brand in brands">
              <a :href="brand.href">{{ brand.title }}</a>
            </div>
          </div>
        </div>
        <div class="my-navbar__buttons">
          <a class="my-navbar__button" href="/for_men">For Men</a>
          <a class="my-navbar__button" href="/for_her">For Her</a>
          <a class="my-navbar__button" href="/discounts">Discount</a>
        </div>
      </div>
      <div class="my-navbar-right">
        <SearchForm class="me-2" />
        <button type="button" class="btn btn-outline-light me-2">Login</button>
        <button type="button" class="btn btn-warning">Sign-up</button>
      </div>
    </div>
  </header>
</template>

<script>
import SearchForm from "../UI/SearchForm";

export default {
  components: {
    SearchForm,
  },
  data() {
    return {
      // replace on real data
      brands: [
        { title: "Tom Ford", href: "/tom_ford" },
        { title: "MFK", href: "/mfk" },
        { title: "De Marly", href: "/de_marly" },
      ],
    };
  },
};
</script>

<style scoped>
@media (max-width: 992px) {
  .main {
    max-width: 325px;
  }
}

/* Dropdown Button */
.dropdown-btn {
  background-color: rgba(28, 28, 28, 0);
  border: none;
  text-decoration: none;
  color: rgb(168, 168, 168);
  font-size: 18px;
}

.dropdown-btn:hover {
  color: white;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.my-navbar__button {
  text-decoration: none;
  color: rgb(168, 168, 168);
  font-size: 18px;
  padding: 10px;
}
.my-navbar__button:hover {
  color: rgb(255, 255, 255);
}
.shop-name {
  text-decoration: none;
  color: white;
  font-size: 25px;
  padding-right: 15px;
}
.my-navbar {
  display: flex;
  justify-content: space-between;
}
.my-navbar-left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.my-navbar-right {
  display: flex;
  flex-direction: row;
}
</style>
