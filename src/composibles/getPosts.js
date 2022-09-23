import { ref } from "vue";
import axios from 'axios'
const getPosts = (id) => {
    const posts = ref([]);

    const load = async () => {
        try {
            let { data } = await axios("http://localhost:3003/posts",id)
            console.log("posts",data);
            posts.value = data
        } catch (error) {
            console.log(error)
        }
    }


    return { posts, load }
}

export default getPosts