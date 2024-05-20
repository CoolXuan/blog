<template>
  <div class="post-list">
    <div name="imc" v-for="post in posts" :key="post[0]">
      <SinglePost :post="post" @dblclick="delPost(post[0])" />
    </div>
  </div>
</template>
<script setup>
import SinglePost from "./SinglePost.vue";
import axios from 'axios'
let prop = defineProps({
  posts: { type: Array },
});
let delPost = async function (id) {
  prop.posts=await axios.delete("/api/posts/"+id);
  location.reload()
}

</script>



<style scoped>
.imc-enter-from {
  opacity: 0;
}

.imc-enter-to {
  opacity: 1;
}

.imc-leave-from {
  opacity: 1;
}

.imc-leave-to {
  opacity: 0;
}

.imc-enter-active {
  transition: opacity 5s ease;
}

.imc-leave-active {
  transition: opacity 5s ease;
}
</style>
