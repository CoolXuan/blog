<template>
    <div class="videodown-main">
        <div class="searchcontainer">
            <input v-model="searchContent" placeholder="请输入视频链接" type="text" class="search">
            <button class="btnsearch" @click="searchVideo">搜索</button>
        </div>
        <div>
        </div>
        <div class="main-content">
            <div class="bilibili">
                <div class="platform-content">
                    <div class="title">
                        <div class="title-header">哔哩哔哩</div>
                        <img class="title-img" src="../assets/bilibili.png" />
                    </div>
                    <div class="tool-content">
                        <div class="tool-content-item">
                            <!-- 视频信息 -->
                            <div class="video-info">
                                <img src="../assets/bilibili.png" class="img-info">
                                <div class="video-header-info">
                                    <div class="video-header">{{ downloadVideoTitle.slice(0, 34) + "..." }}</div>
                                    <div class="video-definition">1080P</div>
                                </div>
                                <button class="video-download" @click="downloadVideo">下载</button>
                            </div>
                            <!-- 下载进度 -->
                            <div class="download-process">
                                <div class="process-bar">
                                    <div class="process-bar-tip"><span>音频下载：</span><span>{{ audio_loadedData[0]
                                            }}Mb/{{ audio_totalData[0] }}Mb</span></div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar"
                                                :style="`background-color:var(--theme-bili);width:${audioProgress}%;`">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="process-bar-tip"><span>视频下载：</span><span>{{ video_loadedData[0]
                                            }}Mb/{{ video_totalData[0] }}Mb</span>
                                    </div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar"
                                                :style="`background-color:var(--theme-bili);width:${videoProgress}%;`">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button class="btn-combine">合并</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="douyin">
                <div class="platform-content">
                    <div class="title">
                        <div class="title-header">抖音</div>
                        <img class="title-img" src="../assets/douyin.png" />
                    </div>
                    <div class="tool-content">
                        <div class="tool-content-item">
                            <!-- 视频信息 -->
                            <div class="video-info">
                                <img src="../assets/douyin.png" class="img-info">
                                <div class="video-header-info">
                                    <div class="video-header">2132132132132132132</div>
                                    <div class="video-definition">1080P</div>
                                </div>
                                <button class="video-download">下载</button>
                            </div>
                            <!-- 下载进度 -->
                            <div class="download-process">
                                <div class="process-bar">
                                    <div class="process-bar-tip">音频下载：</div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar"
                                                :style="`background-color:var(--theme-douyin);width:${60}%;`">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="process-bar-tip">视频下载：</div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar"
                                                :style="`background-color: var(--theme-douyin);width:${78}%;`">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button class="btn-combine">合并</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="kuaishou">
                <div class="platform-content">
                    <div class="title">
                        <div class="title-header">快手</div>
                        <img class="title-img" src="../assets/kuaishou.png" />
                    </div>
                    <div class="tool-content">
                        <div class="tool-content-item">
                            <!-- 视频信息 -->
                            <div class="video-info">
                                <img src="../assets/kuaishou.png" class="img-info">
                                <div class="video-header-info">
                                    <div class="video-header">2132132132132132132</div>
                                    <div class="video-definition">1080P</div>
                                </div>
                                <button class="video-download">下载</button>
                            </div>
                            <!-- 下载进度 -->
                            <div class="download-process">
                                <div class="process-bar">
                                    <div class="process-bar-tip">音频下载：</div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar" style="background-color: var(--theme-kuaishou);">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="process-bar-tip">视频下载：</div>
                                    <div class="container">
                                        <div class="progress progress-striped">
                                            <div class="progress-bar" style="background-color: var(--theme-kuaishou);">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button class="btn-combine">合并</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { FFmpeg } from '@ffmpeg/ffmpeg';
const ffmpeg = new FFmpeg()
const downloadVideoTitle = ref("");
const audioProgress = ref(0);
const videoProgress = ref(0);
const audio_loadedData = ref(0)
const video_loadedData = ref(0)
const audio_totalData = ref(0)
const video_totalData = ref(0)
const searchContent = ref("https://www.bilibili.com/video/BV1mz421y7hJ/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=75585aa1804f86de170e160f77e7547b");
let searchVideo = () => {
    axios.post('/api/v/bili', { "data": searchContent.value }).then((data) => {
        console.log(data.data)
        let videoInfo = {
            title: data.data.title[0],
            audio_url: data.data.audio_url,
            video_url: data.data.video_url
        }
        sessionStorage.setItem(videoInfo.title, JSON.stringify(videoInfo))
        downloadVideoTitle.value = JSON.parse(sessionStorage.getItem(videoInfo.title)).title;
    })

}
let downloadVideo = () => {
    if (downloadVideoTitle.value != "") {
        downloadFile(JSON.parse(sessionStorage.getItem(downloadVideoTitle.value)).audio_url, JSON.parse(sessionStorage.getItem(downloadVideoTitle.value)).title, 'm4s', 'audio');
        downloadFile(JSON.parse(sessionStorage.getItem(downloadVideoTitle.value)).video_url, JSON.parse(sessionStorage.getItem(downloadVideoTitle.value)).title, 'm4s', 'video');
    } else {
        alert("请先搜索视频！")
    }

}
let downloadFile = (url, title, fomat, type) => {
    axios({
        method: 'get',
        url: url,
        responseType: 'blob',
        onDownloadProgress: (evt) => {
            // 对原生进度事件的处理
            if (fomat == "m4s") {
                if (type == "audio") {
                    audio_loadedData.value = (parseInt(evt.loaded) / 1024 / 1024).toString().match(/^\d+(?:\.\d{0,2})?/)
                    audio_totalData.value = (parseInt(evt.total) / 1024 / 1024).toString().match(/^\d+(?:\.\d{0,2})?/)
                    audioProgress.value = parseInt((evt.loaded / evt.total) * 100)
                }
                if (type == "video") {
                    video_loadedData.value = (parseInt(evt.loaded) / 1024 / 1024).toString().match(/^\d+(?:\.\d{0,2})?/)
                    video_totalData.value = (parseInt(evt.total) / 1024 / 1024).toString().match(/^\d+(?:\.\d{0,2})?/)
                    videoProgress.value = parseInt((evt.loaded / evt.total) * 100)
                }

            }
        }
    }).then(res => {
        let data = res.data // 这里后端对文件流做了一层封装，将data指向res.data即可
        console.log(data);
        if (!data) {
            return
        }
        let url = window.URL.createObjectURL(new Blob([data]))
        let a = document.createElement('a')
        a.style.display = 'none'
        a.href = url
        a.setAttribute('download', title + '.' + fomat)
        document.body.appendChild(a)
        a.click() //执行下载
        window.URL.revokeObjectURL(a.href) //释放url
        document.body.removeChild(a) //释放标签
    }).catch((error) => {
        console.log(error)
    })
}
let combineFile = async () => {
    // 加载ffmpeg核心
    // messageText.value = '加载ffmpeg-core.js';
    await ffmpeg.load({
        coreURL: '/static/esm/ffmpeg-core.js',
        // wasmURL: '/static/esm/ffmpeg-core.wasm'
    });

    await ffmpeg.writeFile('test.m4s', await fetchFile('/static/shopDetail.m4s'));
    await ffmpeg.exec(['-i', 'test.m4s', 'test.mp4']);
    const data = await ffmpeg.readFile('test.mp4');
    videoSrc.value = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
}
</script>
<style lang="scss" scoped>
.videodown-main {
    display: flex;
    flex-direction: column;

    /* 外部盒子,控制搜索框在页面中的位置 */
    .searchcontainer {
        margin: 0 auto;
        height: 100px;
        display: flex;
        justify-content: center;
        /*水平方向居中*/
        align-items: center;
        /*垂直方向居中*/
        background-color: white;

        /* 搜索框样式 */
        .search {
            width: 90%;
            height: 45px;
            background-image: url(../assets/search.png);
            background-size: 25px;
            /*搜索框背景图片*/
            background-repeat: no-repeat;
            /*设置背景图片不平铺*/
            border-radius: 5px 0px 0px 5px;
            padding-left: 40px;
            background-position: 10px 10px;
            /*设置背景图片的位置*/
            color: darkgray;
            font-size: 18px;
            border: #ff5900 solid 1px;
            /*去除边框*/
        }

        /* 搜索框获得焦点时样式 */
        .search:focus {
            outline: black solid 1px;
            /*添加外边框*/
        }

        /* 搜索按钮样式 */
        .btnsearch {
            width: 10%;
            height: 51px;
            border: none;
            background-color: black;
            color: #fff;
            border-radius: 0px 5px 5px 0px;
            font-size: 20px;
            cursor: pointer;
        }

        /* 按钮悬浮时样式 */
        .btnsearch:hover {
            background-color: #ff5900;
        }
    }

    .main-content {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;


        .bilibili {
            background-color: var(--theme-bili);
            border-radius: 5px;
        }

        .douyin {
            background-color: var(--theme-douyin);
            border-radius: 5px;
        }

        .kuaishou {
            background-color: var(--theme-kuaishou);
            border-radius: 5px;
        }

        .platform-content {
            width: 450px;
            height: 600px;

            .title {
                width: 100%;
                height: 30px;
                padding-left: 10px;
                line-height: 30px;
                color: var(--theme-white);
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
                justify-content: space-between;

                .title-header {
                    font-size: 16px;
                    font-weight: 600;
                }

                .title-img {
                    padding-right: 20px;
                    width: 25px;
                    height: 25px;
                }
            }

            .tool-content {
                border-radius: 5px;
                width: 100%;
                height: 580px;
                background-color: var(--theme-grey);

                .tool-content-item {
                    margin: 0 auto;
                    width: 98%;
                    height: auto;

                    background-color: white;
                    display: flex;
                    flex-direction: column;

                    .video-info {
                        width: 100%;
                        height: 50px;
                        display: flex;
                        flex-direction: row;
                        justify-content: center;
                        align-items: center;

                        .img-info {
                            width: 40px;
                            height: 40px;
                        }

                        .video-header-info {
                            padding-left: 10px;
                            padding-right: 10px;
                            background-color: white;
                            display: flex;
                            flex-direction: column;
                            flex: 6;

                            .video-header {
                                font-size: 18px;
                                font-weight: bold;
                            }

                            .video-definition {
                                font-size: 12px;
                                color: grey;

                            }
                        }

                        .video-download {
                            font-size: 13px;
                            background-color: #fff;
                            border-radius: 5px;
                            font-weight: bold;
                            text-align: center;
                            width: 45px;
                            height: 45px;
                        }

                        .video-download:hover {
                            color: #fff;
                            background-color: var(--theme-bili);
                        }
                    }

                }

                .download-process {
                    width: 100%;
                    height: 60px;
                    display: flex;
                    flex-direction: row;
                    justify-content: center;
                    align-items: center;
                    border-top: 1px solid var(--theme-grey);

                    .process-bar {
                        display: flex;
                        flex-direction: column;
                        flex: 1;
                        $background: #2c303a;

                        .process-bar-tip {
                            display: flex;
                            flex-direction: row;
                            justify-content: space-between;
                            margin-right: 10px;
                            font-size: 10px;
                            color: grey;
                        }

                        .container {
                            width: 98%;
                            text-align: center;

                            .progress {
                                padding: 2px;
                                background: rgba(0, 0, 0, 0.25);
                                border-radius: 2px;
                                box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.25), 0 1px rgba(255, 255, 255, 0.08);

                                .progress-bar {
                                    height: 6px;
                                    background-color: var(--theme-bili);
                                    border-radius: 2px;

                                }
                            }

                            .progress-striped .progress-bar {
                                transition: 0.4s linear;
                                transition-property: width, background-color;
                                //     background-image: linear-gradient(45deg, var(--theme-green) 25%,
                                //             transparent 10%, transparent 50%,
                                //             var(--theme-green) 50%, var(--theme-bili) 75%,
                                //             transparent 75%, transparent);
                            }
                        }
                    }

                    .btn-combine {
                        font-size: 13px;
                        background-color: #fff;
                        border-radius: 5px;
                        font-weight: bold;
                        text-align: center;
                        width: 45px;
                        height: 45px;
                    }

                    .btn-combine:hover {
                        color: #fff;
                        background-color: var(--theme-green);
                    }

                }
            }
        }
    }
}
</style>