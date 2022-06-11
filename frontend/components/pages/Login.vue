<template>
  <div class="login">
    <img class="off-logo" src="../source/official_logo.jpg" alt="spicyPerfume">
    <div class="signin-form">
      <form class="block-signin">
        <h3>Please sign in</h3>
        <div class="inputs">
          <div class="form-floating">
            <input
              v-model="email"
              type="email"
              class="form-control"
              placeholder="name@example.com"
            />
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating">
            <input
            v-model="password"
              type="password"
              class="form-control"
              placeholder="Password"
            />
            <label for="floatingPassword">Password</label>
          </div>
        </div>
        <button
          class="w-100 btn btn-lg btn-primary mt-4 signin-button"
          type="submit"
          @click="signIn"
        >
          Sign in
        </button>
      </form>
    </div>
    <div class="alter-signin">
      <h6 class="text-or">OR</h6>
      <div class="images">
        <img src="../source/google.png">
        <img src="../source/vk.png">
        <img src="../source/facebook.png">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    signIn() {
      // create a validator for email and password
      // !!! create hashed password !!!
      // post request to login here
      // sned request in JSON format
    }
  }
};
</script>

<style scoped>
.login {
  background-color: #fff;
  display: flex;  
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex: 1 1 auto;
  padding-bottom: 100px;
}
.off-logo {
  margin: 25px 0;
  width: 125px
}
.signin-form {
  display: flex;
  flex-direction: row;
}
.inputs {
  overflow: hidden;
  min-width: 300px;
  border: none;
  border: solid 1px #ccc;
  border-radius: 15px;
}
.inputs > input {
  height: 50px;
}
.signin-button {
  border-radius: 10px;
}
.block-signin {
  display: flex;
  flex-direction: column;
  align-items: center;
} 
.alter-signin {
  display: flex;
  flex-direction: column;
  margin-top: 25px;
  align-items: center;
}
.text-or {
  color: gray;
}
.images {
  display: flex;
  margin-top: 7px;
}
.images > img {
  height: 30px;
  width: 30px;
  cursor: pointer;
  margin: 0 5px 0 5px;
}
</style>
