<script setup>
import { computed, ref } from "vue";
const props = defineProps({
  post: Array,
});
console.log(props.post);
const snippet = computed(() => {
  return props.post[2] + "...";
});
</script>

<template>
  <div class="post">
    <router-link :to="{ name: 'Details', params: { id: post[0] } }">
      <h3>{{ post[1] }}</h3>
    </router-link>
    <br>
    <!-- <p v-html="snippet"></p> -->
    <div class="tags">
      <div>#{{ post[3] }}</div>
      <div>发表于{{ post[4] }}</div>
      <div> 来源于<span class="author">{{ post[5] }}</span></div>
    </div>

  </div>
</template>


<style scoped>
.post {
  padding-left: 20px;
  padding-right: 20px;
  border-radius: 5px;
  background-color: rgb(246, 145, 221);
  color: black;
  margin: 0 10px 10px;
  padding-bottom: 30px;
  border-bottom: 1px dashed #e7e7e7;
  opacity: 0.6;
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.4s;
  -webkit-transition-property: box-shadow, transform;
  transition-property: box-shadow, transform;
}

.post:hover {
  transform: scale(1.06);
  background-color: rgb(246, 145, 221);
  color: rgb(30, 16, 62);
  opacity: 1;
  box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.5);
  -webkit-transform: scale(1.06);
}

.post h3 {
  display: inline-block;
  position: relative;
  font-size: 20px;
  color: rgb(9, 9, 9);
  margin-bottom: 10px;
  max-width: 400px;
}

.post h3::before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
  padding-right: 40px;
  left: -30px;
}

.post span {
  font-size: 10px;
}
.tags{
  display: flex;
  flex-direction: row;
  justify-content:space-between ;
}
.author{
  font-size: 50px;
  font-weight: 600;
  color: aqua;
}
</style>