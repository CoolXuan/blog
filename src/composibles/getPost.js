import { ref } from "vue";
import axios from 'axios'
const getPost = (id) => {
    const post = ref({});
    const load = async () => {
        try {
            let data  = await axios.get("/api/post/" + id)
            post.value = data.data
        } catch (error) {
            console.log(error)
        }
    }

    return { post, load }
}

export default getPost