import Main from "../components/pages/Main";
import Login from "../components/pages/Login";
import SignUp from "../components/pages/SignUp";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/signup",
    component: SignUp,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

export default router;
