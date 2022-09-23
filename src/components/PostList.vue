<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id">
      <SinglePost :post="post" />
    </div>
  </div>
</template>
<script setup>
import SinglePost from "./SinglePost.vue";
// import delPosts from '../composibles/delPosts'
import axios from 'axios'
let xxx = defineProps({
  posts: { type: Array },
});
// function del(id) {
//   console.log("xxx", xxx.posts);
//   console.log("del", id);
//   xxx.posts.forEach(function (item) {
//     //   //返回符合条件的数组
//     // if (item.id===id) {
//     //   const data = await axios("http://localhost:3003/posts", id);
//     //   if (data.status === 201) {
//     //     router.push("/");
//     //   }
//     // }

//   })
//   //   console.log(arr);

// }

</script>



<style>

</style>
