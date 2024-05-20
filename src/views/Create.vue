<template>
  <div class="create">
    <form @submit.prevent="handleSubmit">
      <label for="title">标题</label>
      <input type="text" v-model="title" required  />
      <label for="body">内容</label>
      <QuillEditor  style="height: 300px; margin-bottom: 10px" content-type="html" v-model:content= "content" :toolbar="options.modules.toolbar" />
     标签<input type="text" v-model="tag" @keydown.enter.prevent="handleKeydown" />

      <!-- 显示标签 -->
      <div class="showInfo">
        <div v-for="tag in tags" :key="tag" class="pill">#{{ tag }}</div>
      </div> <span class="list">发表时间：{{current_time}}</span>
      <button>添加</button>
    </form>
  </div>
</template>
<script setup>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { ref, onMounted, reactive } from "vue";
import axios from "axios";
import options from './editorjs/quilOptions.js'
// import 'highlight.js/styles/monokai-sublime.css'
import { useRouter } from "vue-router";
// import { titleConfig } from './editorjs/titleConfig.js' // 富文本文本提示

const title = ref("");
const content = ref('')
const tags = ref([]);
const tag = ref("");
const current_time = ref("");
const router = useRouter();
// const editorOption = reactive({})


const handleKeydown = () => {
  if (!tags.value.includes(tag.value)) {
    tag.value = tag.value.replace(/\s/g, "");
    tags.value.push(tag.value);
  }

  tag.value = "";
};
const getCurrentTime = function () {
  var date = new Date();
  var year = date.getFullYear(); //当前年份
  var month = date.getMonth(); //当前月份
  var data = date.getDate(); //天
  var hours = date.getHours(); //小时
  var minute = date.getMinutes(); //分
  var second = date.getSeconds(); //秒
  current_time.value = year + "-" + (month + 1) + "-" + data + "      " + hours + ":" + minute + ":" + second;
}
onMounted(() => {
  let myTimeDisplay = null
  getCurrentTime();
  clearInterval(myTimeDisplay);
  myTimeDisplay = setInterval(() => {
    getCurrentTime(); //每秒更新一次时间  
  }, 1000);

})
// watch(() => { value }, (newval, oldval) => {
//   console.log(newval, oldval);
// })
const handleSubmit = async () => {
  //获取当前时间

  // 准备数据
  const post = {
    id: Math.floor(Math.random() * 10000),
    title: title.value,
    body: content.value,
    tags: tags.value,
    current_time: current_time.value,
    author:sessionStorage.getItem("userName")
  };
console.log(post);
  const data = await axios.post("/api/posts", post);
  console.log(data.data);
  if (data.data === 'submit-success') {
    router.push("/");
  }
}
</script>
<style lang="scss" scoped>
form {
  max-width: 1000px;
  margin: 0 auto;
  // text-align: left;
}

input,
textarea {
  display: block;
  margin: 10px 0;
  width: 50%;
  box-sizing: border-box;
  padding: 10px;
  border: 3px solid rgb(30, 53, 223);
  border-radius: 5px;
  background-color: rgb(136, 74, 74,0);
}

textarea {
  height: 160px;
}

label {
  display: inline-block;
  margin-top: 30px;
  position: relative;
  font-size: 20px;
  margin-bottom: 10px;
}

button {
  border-radius: 5px;
  display: block;
  margin-top: 30px;
  background: #ff00e1;
  color: white;
  border: none;
  padding: 8px 16px;
  font-size: 18px;
}

.list {
  transform: scale(0.4);
}

.pill {
  display: inline-block;
  margin: 10px 10px 0 0;
  color: #444;
  background: #ddd;
  padding: 8px;
  border-radius: 20px;
  font-size: 14px;
}
.create{
  padding-left: 10px;
}
.vue-quill-editor {
  .quill-editor {
    line-height: normal;

    .ql-container.ql-snow {
      line-height: normal !important;
      height: 550px !important;
      font-size: 14px;
    }

    .ql-snow {
      .ql-tooltip[data-mode=link]::before {
        content: "请输入链接地址:";
      }

      .ql-tooltip.ql-editing a.ql-action::after {
        border-right: 0px;
        content: '保存';
        padding-right: 0px;
      }

      .ql-tooltip[data-mode=video]::before {
        content: "请输入视频地址:";
      }

      .ql-picker.ql-size {

        .ql-picker-label[data-value="12px"]::before,
        .ql-picker-item[data-value="12px"]::before {
          content: '12px';
        }

        .ql-picker-label[data-value="14px"]::before,
        .ql-picker-item[data-value="14px"]::before {
          content: '14px';
        }

        .ql-picker-label[data-value="16px"]::before,
        .ql-picker-item[data-value="16px"]::before {
          content: '16px';
        }

        .ql-picker-label[data-value="18px"]::before,
        .ql-picker-item[data-value="18px"]::before {
          content: '18px';
        }

        .ql-picker-label[data-value="20px"]::before,
        .ql-picker-item[data-value="20px"]::before {
          content: '20px';
        }

        .ql-picker-label[data-value="24px"]::before,
        .ql-picker-item[data-value="24px"]::before {
          content: '24px';
        }

        .ql-picker-label[data-value="28px"]::before,
        .ql-picker-item[data-value="28px"]::before {
          content: '28px';
        }

        .ql-picker-label[data-value="32px"]::before,
        .ql-picker-item[data-value="32px"]::before {
          content: '32px';
        }

        .ql-picker-label[data-value="36px"]::before,
        .ql-picker-item[data-value="36px"]::before {
          content: '36px';
        }
      }

      .ql-picker.ql-header {

        .ql-picker-label::before,
        .ql-picker-item::before {
          content: '文本';
        }

        .ql-picker-label[data-value="1"]::before,
        .ql-picker-item[data-value="1"]::before {
          content: '标题1';
        }

        .ql-picker-label[data-value="2"]::before,
        .ql-picker-item[data-value="2"]::before {
          content: '标题2';
        }

        .ql-picker-label[data-value="3"]::before,
        .ql-picker-item[data-value="3"]::before {
          content: '标题3';
        }

        .ql-picker-label[data-value="4"]::before,
        .ql-picker-item[data-value="4"]::before {
          content: '标题4';
        }

        .ql-picker-label[data-value="5"]::before,
        .ql-picker-item[data-value="5"]::before {
          content: '标题5';
        }

        .ql-picker-label[data-value="6"]::before,
        .ql-picker-item[data-value="6"]::before {
          content: '标题6';
        }
      }

      .ql-picker.ql-font {

        .ql-picker-label[data-value="SimSun"]::before,
        .ql-picker-item[data-value="SimSun"]::before {
          content: "宋体";
          font-family: "SimSun" !important;
        }

        .ql-picker-label[data-value="SimHei"]::before,
        .ql-picker-item[data-value="SimHei"]::before {
          content: "黑体";
          font-family: "SimHei";
        }

        .ql-picker-label[data-value="Microsoft-YaHei"]::before,
        .ql-picker-item[data-value="Microsoft-YaHei"]::before {
          content: "微软雅黑";
          font-family: "Microsoft YaHei";
        }

        .ql-picker-label[data-value="KaiTi"]::before,
        .ql-picker-item[data-value="KaiTi"]::before {
          content: "楷体";
          font-family: "KaiTi" !important;
        }

        .ql-picker-label[data-value="FangSong"]::before,
        .ql-picker-item[data-value="FangSong"]::before {
          content: "仿宋";
          font-family: "FangSong";
        }
      }
    }

    .ql-align-center {
      text-align: center;
    }

    .ql-align-right {
      text-align: right;
    }

    .ql-align-left {
      text-align: left;
    }
  }
}
</style>