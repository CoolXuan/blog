import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Details from '../views/Details.vue'
import Create from '../views/Create.vue'
import Tags from '../views/Tag.vue'
import VideoDownload from '../views/VideoDownload.vue'
import MusicDownload from '../views/MusicDownload.vue'
import Coupons from '../views/Coupons.vue'


const routes = [
    { path: "/", name: 'Home', component: Home },
    { path: "/posts/:id", name: 'Details', component: Details, props: true },
    { path: "/create", name: 'Create', component: Create },
    { path: "/videodownload", name: 'VideoDownload', component: VideoDownload },
    { path: "/musicdownload", name: 'MusicDownload', component: MusicDownload },
    { path: "/coupons", name: 'Coupons', component: Coupons },
    { path: "/tags/:tag", name: 'Tag', component: Tags },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router;