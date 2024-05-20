<script setup>
import axios from 'axios'
import { ref, onMounted, reactive, watch } from 'vue'
const active = ref(false)
const exchange1 = ref(true);
const exchange2 = ref(false);
const check = ref(false);
const warning_msg = ref("");
const pwd = ref("");
const repwd = ref("");
const email = ref("");
const code = ref("");
const user_name = sessionStorage.getItem('userName') || ref("登录");
const xxx = defineProps({
  show: Boolean
})
watch(
  () => {
    xxx.show;
  },
  () => {
    active.value = xxx.show
  },
  {
    immediate: true,
    deep: true,
  }
);
const userState = reactive({
  email: "1976756410@qq.com",
  pwd: "123456",
  repwd: "123456789a",
});
function initmsg() {
  // msg数据初始化
  // id = ''
  userState.email = "";
  userState.pwd = "";
  userState.repwd = "";
}
let loseAim = function () {
  initmsg();
  active.value = false;
};
function login() {
  // if (userState.email.match(/^[a-z]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i)) {
  const url = "/api/login";
  let param = {
    "email": userState.email,
    "password": userState.pwd
  }
  axios.post(url, param).then((res) => {
    user_name.value = res.data;
    if (user_name.value !== "not exist") {
      active.value = !active.value;
      sessionStorage.setItem("userName", user_name.value);
      alert("登录成功，欢迎" + user_name.value);
      location.reload()
      initmsg();

    } else {
      alert("登录失败，可能此账号未注册！");
    }
  });
  // } else {
  //   alert("邮箱格式不匹配！");
  // }
}
function getcode() {
  // console.log("get-code");
  // if (userState.email.match("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")) {
  const url = "/api/ecode/" + userState.email;
  axios.post(url).then((data) => {
    console.log(data.data)
    data = data.data;
    if (data === "email-invalid") {
      alert("邮箱地址格式不正确.");
      return false;
    }
    if (data === "send-pass") {
      alert("邮箱验证码已成功发送，请查收.");
      return false;
    }
    if (data === "user-repeated") {
      userState.email = "";
      userState.pwd = "";
      userState.repwd = "";
      alert("邮箱已注册，请重新输入其他邮箱！");
      return false;
    }
    if (data === "send-fail") {
      alert("邮箱验证码未发送成功.");
      return false;
    }
  });
}
function change1() {
  exchange1.value = true;
  exchange2.value = false;
  // initmsg();
}
function change2() {
  exchange1.value = false;
  exchange2.value = true;
  // initmsg();
}
let turnMask = function () {
  active.value = !active.value;
}
function denglu() {
  // initmsg();
  if (sessionStorage.getItem('userName')) {
    alert('您的账号已登录，无需再次登录')
  } else {
    active.value = !active.value;
  }
}
// audio_url
// : 
// "https://xy120x241x124x9xy.mcdn.bilivideo.cn:8082/v1/resource/1492640632-1-30280.m4s?agrr=0&build=0&buvid=13BDB6B0-42D9-394C-4854-62C0E45A03E053164infoc&bvc=vod&bw=19478&deadline=1712637252&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=80000000&mid=0&nbs=1&nettype=0&oi=0&orderid=0%2C3&os=08cbv&platform=pc&sign=6704db&traceid=trOQHPRMAGnYgW_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=253a801f0591da935951a3bf9d698e06"
// title
// : 
// ['【阿斗】3000万成本斩获近8亿票房！口碑票房双逆袭，名场面无数的小成本黑马喜剧《无名之辈》']
// video_url
// : 
// "https://xy106x111x237x1xy.mcdn.bilivideo.cn:8082/v1/resource/1492640632-1-100047.m4s?agrr=0&build=0&buvid=13BDB6B0-42D9-394C-4854-62C0E45A03E053164infoc&bvc=vod&bw=45097&deadline=1712637252&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=80000000&mid=0&nbs=1&nettype=0&oi=0&orderid=0%2C3&os=08cbv&platform=pc&sign=c63b9d&traceid=tryYkiJpMuMFnV_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=293410cdbf52c28b7b772802984b6584"


let downloadFile = (url,title,fomat) => {
  axios({
    method: 'get',
    url: url,
    responseType: 'blob',
    onDownloadProgress: (evt) => {
        // console.log("progressEvent===",evt )
        // 对原生进度事件的处理
        downloadProgress.value=parseInt((evt.loaded / evt.total) * 100) 
      }
  }).then(res => {
    let data = res.data // 这里后端对文件流做了一层封装，将data指向res.data即可
    if (!data) {
      return
    }
    let url = window.URL.createObjectURL(new Blob([data]))
    let a = document.createElement('a')
    a.style.display = 'none'
    a.href = url
    a.setAttribute('download', title+'.'+fomat)
    document.body.appendChild(a)
    a.click() //执行下载
    window.URL.revokeObjectURL(a.href) //释放url
    document.body.removeChild(a) //释放标签
  }).catch((error) => {
    console.log(error)
  })
}
let DownloadBiliBili = () => {
  
}
let zhuce = function () {
  const url = "/api/user/" + userState.email + '&' + userState.pwd + '&' + code.value;
  axios.post(url).then((data) => {
    console.log(data.data)
    data = data.data;
    if (data !== "ecode-error") {
      user_name.value = data
      alert('欢迎用户' + user_name.value + '的加入！')
      active.value = !active.value;
    } else {
      alert("验证码错误，请重新输入！");
    }
  });
}
let layout = function () {
  sessionStorage.removeItem('userName');
  location.reload()
}
watch(
  () => {
    userState.pwd;
  },
  () => {
    if (userState.pwd !== userState.repwd) {
      userState.warning_msg = "确认密码不一致！";
      check.value = true;
    } else if (pwd.value === repwd.value) {
      if (!pwd.value.match(/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9a-zA-Z]{8,12}$/)) {
        warning_msg.value = "密码必须是8-12位且包含数值和字母！";
      } else {
        check.value = false;
      }
    }
  },
  {
    immediate: true,
    deep: true,
  }
);
const time = ref('')
let loveTime = function () {
  let new_date = new Date(); //新建一个日期对象，默认现在的时间
  let old_date = new Date("2020-09-25 13:00:00"); //设置过去的一个时间点，"yyyy-MM-dd HH:mm:ss"格式化日期
  let difftime = new_date - old_date; //计算时间差
  let day = Math.floor(difftime / 1000 / (3600 * 24))
  let ms = difftime / 1000 % (3600 * 24)
  let h = Math.floor(ms / 3600)
  let m = Math.floor(ms % 3600 / 60)
  let s = Math.floor(ms % 3600 % 60)
  time.value = `我们相爱了${day}天${h}小时${m}分钟${s}秒`
}
onMounted(() => {
  let myTimeDisplay = null
  loveTime()
  clearInterval(myTimeDisplay);
  myTimeDisplay = setInterval(() => {
    loveTime(); //每秒更新一次时间  
  }, 1000);
})
</script>

<template>
  <div class="box" v-if="active" @blur="loseAim">
    <h2>
      <span @click="change1">登录</span>|<span @click="change2">注册</span>
    </h2>
    <div class="login" v-if="exchange1" method="GET">
      <div class="inputBox">
        <label>账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
        <input type="text" placeholder="请输入电话号码/Email" v-model="userState.email" class="login_input" />
      </div>
      <div class="inputBox">
        <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
        <input class="login_input" type="password" name="" v-model="userState.pwd" />
      </div>
      <input type="submit" class="submit" value="登录" @click="login" />
    </div>
    <div class="register" v-if="exchange2">
      <div class="inputBox">
        <label>账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
        <input type="text" class="login_input" placeholder="请输入电话号码/Email" v-model="userState.email" />
      </div>
      <div class="inputBox">
        <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
        <input class="login_input" type="password" name="" v-model="userState.pwd" /><br />
      </div>
      <div class="inputBox">
        <label>确认密码</label>
        <input class="login_input" type="text" name="" v-model="userState.repwd" />
      </div>
      <div class="inputBox">
        <label>验&nbsp;&nbsp;证&nbsp;&nbsp;码</label>
        <input class="login_input" type="text" name="" style="width: 4rem" v-model="code" />
        <input class="send_email" type="submit" value="发送邮件" @click="getcode" />
      </div>
      <div class="ok" v-if="check">{{ warning_msg }}</div>
      <input type="submit" class="submit" value="注册" @click="zhuce" />
    </div>
  </div>
  <header>
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/create" class="createBtn">发布</router-link>
      <router-link to="/videodownload" class="createBtn">视频下载</router-link>
      <router-link to="/musicdownload" class="createBtn">音乐下载</router-link>
      <router-link to="/coupons" class="createBtn">外卖领券</router-link>
    </nav>
    <h2>工具箱 
      <!-- <input type="text" class="login_input" v-model="urlBili" /><span>{{ downloadProgress }}</span><button @click="DownloadBiliBili">下载</button>
      <input type="text" v-model="downloadVideoTitle" class="login_input" /> -->
    </h2>
    <h4><span @click="denglu" class="layin">{{ user_name }}</span>💜<span @click="layout" class="layout">登出 </span> 博客
    </h4>
    <!-- <span>{{ time }}</span>  -->


  </header>
  <div v-if="active" class="mask" @click="turnMask"></div>
</template>

<style lang="scss" scoped>
.login_input {
  padding-left: 10px;
  font-weight: 600;
  font-size: 18px;
}

.layin {
  color: var(--theme-blue);
}

.mask {
  position: fixed;
  background-color: rgba(255, 255, 255, .1);
  top: 0;
  left: 0;
  backdrop-filter: blur(30px);
  z-index: 3;
  width: 100%;
  height: 100%;
}

header {
  display: flex;
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  justify-content: space-between;
  align-items: center;
  min-width: 100%;
  height: 50px;
  background-color: var(--theme-white);
  border:black 1px solid;
  border-radius: 5px;
}

header h1 {
  color: #271e1e;
  font-size: 48px;
}

header a {
  color: rgb(0, 0, 0);
  text-decoration: none;
  font-size: 14px;
  margin-left: 20px;
}

header a.router-link-active {
  color: #111;
  background-color: rgb(0, 255, 34);
  border-radius: 5px;
  padding: 5px 5px;
  font-size: 18px;
}

.box {
  border-radius: 10px;
  text-align: center;
  // background-color: red;
  position: fixed;
  z-index: 99;
  width: 400px;
  height: 400px;
  top: 25%;
  left: 40%;
  background-color: rgb(241, 160, 230);
  box-shadow: 10px 10px 7px 3px rgb(198, 198, 198);

  .login {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .inputBox {
    margin: 0 auto;
    // margin-bottom: 10px;
    // background-color: #fff;
    display: flex;
    // flex-flow: row;
    flex-direction: row;
    justify-content: center;
    width: 95%;
    // height: 40px;
    font-size: 20px;
    font-family: Arial, Helvetica, sans-serif;

    label {
      font-size: 18px;
      font-weight: 600;
      width: auto;
      line-height: 50px;
    }

    input {
      border: #4b4747 solid 1px;
      margin-left: 10px;
      border-radius: 10px;
      width: 70%;
      height: 40px;
      font-size: 14px;
    }

  }

  .submit {
    width: 60%;
    height: 40px;
    border-radius: 20px;
  }

  .register {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .send_email {
      width: 50%;
      height: 40px;
      font-size: 14px;
      border-radius: 20px solid gray;
      line-height: 0px;
    }
  }
}
</style>
