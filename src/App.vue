<script setup>
import Navbar from './components/Navbar.vue'
import { reactive, ref } from 'vue'
const userName = ref('')
const state = reactive({
  show: false
})
userName.value = sessionStorage.getItem('userName')
let isshow = function () {
  state.show = !state.show
  console.log(state.show);
}
</script>

<template>
  <div>
    <Navbar :show="state.show" />
  </div>
  <div v-if="userName !== null">
    <router-view style="margin-top: 60px;"></router-view>
  </div>
  <div class="noLogin" v-if="!userName">未<span @click="isshow" class="layin">登录</span> </div>
</template>

<style >
:root {
  --bgColor: black;
  --theme-black: #0d2125;
  --theme-white: #ffffff;
  --theme-grey: #d4d4d4;
  --theme-green: #7cea49;
  --theme-red: #ff232e;
  --theme-bili: #ff3171;
  --theme-douyin: #161823;
  --theme-kuaishou: #ff5000;
}

.layin {
  color: aquamarine;
}

.noLogin {
  border-radius: 5px;
  /* margin-top: 10px; */
  max-width: 100%;
  height: 100%;
  margin: 0 auto;
  margin-top: 60px;
  background-color: rgb(226, 134, 211);
  line-height: 800px;
  text-align: center;
  font-size: larger;
}

/* * {
  margin: 0;
  padding: 0;
} */
</style>
