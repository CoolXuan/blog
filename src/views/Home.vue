<script setup>
import PostList from "../components/PostList.vue";
import getPosts from "../composibles/getPosts";
import Spinner from "../components/Spinner.vue";
import TagCloud from "../components/TagCloud.vue";
const { posts,load } = getPosts()
load()
// posts.value=data.data
// console.log(posts.value.length);
</script>

<template>
  <div class="home">
    <div v-if="posts.length" class="layout">
      <PostList :posts="posts" />
      <!-- <TagCloud :posts="posts" /> -->
    </div>
    <div v-else>
      <Spinner />
      <img src="../assets/none.png" class="bgp">
    </div>
  </div>

</template>

<style scoped>
.home {
  max-width: 100%;
  margin: 0 auto;
  padding: 10px;
}

.bgp {
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  border-radius: 5px;
  /* margin-top: 10px; */
  width: 100%;
}

.layout {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 20px;
}
</style>
