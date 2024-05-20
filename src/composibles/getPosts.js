import { ref } from "vue";
import axios from 'axios'
const getPosts = (id) => {
    const posts = ref([]);
    const load = async () => {
        try {
            const data= await axios.get("/api/posts");
            posts.value = data.data
        } catch (error) {
            console.log(error)
        }
    }


    return { posts, load }
}

export default getPosts