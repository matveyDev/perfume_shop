<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top"
    aria-label="Fourth navbar example"
  >
    <div class="container">
      <a class="navbar-brand" href="/">spicyPerfume</a>
      <button
        class="navbar-toggler collapsed"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarsExample04"
        aria-controls="navbarsExample04"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="navbar-collapse collapse" id="navbarsExample04" style="">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="dropdown04"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              >Brands</a
            >
            <ul
              class="dropdown-menu"
              aria-labelledby="dropdown04"
            >
              <div v-for="brand in brands">
                <li>
                  <a 
                    class="dropdown-item" 
                    v-bind:href="brand.href"
                  >{{ brand.title }}
                  </a>
                </li>
              </div>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="/for_men">For Men</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/for_her">For Her</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/discounts">Discounts</a>
          </li>
        </ul>
        <SearchForm/>
        <div>
          <div v-if="true">
            <button type="button" class="btn btn-outline-light me-2">Login</button>
            <button type="button" class="btn btn-warning">Sign-up</button>
          </div>
          <div v-else>
            <button type="button" class="btn btn-outline-light me-2">Profile</button>
          </div>
        </div>
      </div>
    </div>
  </nav>
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
</style>
