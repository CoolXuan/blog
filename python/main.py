import re
from user import User
from article import Article
import json
import requests
from common.utility import gen_email_code, send_email
from flask import Flask, session,jsonify,request,Response
from flask_cors import CORS 
import os
import json
import subprocess
import pymysql
import random
import datetime
from urllib.parse import quote

# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)
CORS(app,supports_credentials=True)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = "1"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

# 登录/注册功能
@app.route('/api/login', methods=['POST']) #登录
def login():
    user = User()
    data=request.get_json()
    # 获取email 和 password
    email = data.get("email")
    password = data.get("password")
    print(email ,password)
    try:
        nickName=user.get_data(email)[0][2]
        return jsonify(nickName)
    except:
        return jsonify('not exist')

@app.route('/api/ecode', methods=['POST']) #检验是否注册
def ecode():
    user = User()
    email = data.get("email")
    # 验证用户是否已经注册
    if len(user.get_data(email)) > 0:
        return 'user-repeated'

    code = gen_email_code()
    send_email(email, code)
    try:
        session['ecode'] = code  # 将邮箱验证码保存在Session中
        print(session['ecode'])
        return 'send-pass'
    except:
        return 'send-fail'

@app.route('/api/user', methods=['POST']) #注册时验证码校验
def register():
    user = User()
    email = data.get("email")
    password = data.get("password")
    ecode = data.get("ecode")
    # 校验邮箱验证码是否正确
    if ecode.lower() != session.get('ecode').lower():
        return 'ecode-error'
    else:
        print('a')
        user_name = user.insert_data(email, password)
        print(user_name)
        if user_name != '':
            return user_name
        # # 更新积分详情表
        return 'reg-pass'


biliheaders = {
    #获取最高清1080p数据,加入cookie个人信息
    'Cookie': 'buvid3=13BDB6B0-42D9-394C-4854-62C0E45A03E053164infoc; b_nut=1682788153; _uuid=7ECAC96D-BDD7-BB46-A1091-DCB108B7E4F1D52773infoc; hit-dyn-v2=1; buvid4=437CE8B5-F794-1D78-D562-5A35186E193C54689-023043001-8tg8EBM5kh3sMLXSa1MWrQ%3D%3D; hit-new-style-dyn=1; CURRENT_PID=f5d25b50-e705-11ed-b31c-f394dfdc49da; rpdid=|(J~RllR~kkm0J''uY)k)kR)Ju; i-wanna-go-back=-1; b_ut=5; buvid_fp_plain=undefined; LIVE_BUVID=AUTO8616828562491882; nostalgia_conf=-1; CURRENT_BLACKGAP=0; FEED_LIVE_VERSION=V8; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=189910467; DedeUserID__ckMd5=5cd08607e3bab812; CURRENT_FNVAL=4048; fingerprint=3dfc0e4a00b0be0658a8a42dead9b580; CURRENT_QUALITY=80; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDg4NzM2MjQsImlhdCI6MTcwODYxNDM2NCwicGx0IjotMX0.9N3p16Ae8DmIc8MQWkOX5-AFaU-J_HwFaXnSI7iKkZw; bili_ticket_expires=1708873564; SESSDATA=17545f0d%2C1724302581%2Ce3ab4%2A22CjBVW1pAEtBN94KdnUkfj8FRHnCKWe4O85HTmNw9pw6nZ64m1FmUVT_S1GwtKIoo0V0SVmxXS01NTTJ2eFZwY3loak1qSFJCVUt6eW1VVklxaUFPQUVvdjdRTFdOeFY0dWJ1MHAzeElsajhlNnNJNng0Y2pjOGJsOFA0WXZTaGpBWWZ4MDJXX2h3IIEC; bili_jct=2b62c22b97bb0f12fe86ee02f0f1d26e; buvid_fp=3dfc0e4a00b0be0658a8a42dead9b580; bp_video_offset_189910467=901949574878330885; b_lsid=16469BF10_18DDEFA63CC; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=5; browser_resolution=1536-714; sid=6fb5ixqo; PVID=1'
    ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    ,
    'referer': 'https://www.bilibili.com/'
}

ksheaders = {
        'Cookie': 'kpf=PC_WEB; clientid=3; did=web_713774521487450db89fcfc3892aae65; didv=1705562481178; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjQzOTc2MzU1LjE3MDU1NjM4MDkxNTEuNzUzNzYy|MS43NjQ1ODM2OTgyODY2OTgyLjk2MjU0NDIxLjE3MDU1NjM4MDkxNTEuNzUzNzYz|0|graphql-server|webservice|false|NA; kpn=KUAISHOU_VISION',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
api_url = "https://api.douyin.com/aweme/v1/feed/"


dyheaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "application/json",
    "Authorization": "Bearer <YOUR_API_TOKEN>"
}

@app.route('/api/v/bili',methods=['POST'])
def biliDownload():
    biliUrl=request.get_json()["data"]
    print(biliUrl)
    if not os.path.exists('./b_video'):
        os.mkdir('./b_video')
    if not os.path.exists('./b_video/temp'):
        os.mkdir('./b_video/temp')
    response=requests.get(url=biliUrl,headers=biliheaders)
    # 获取网页源码
    content=response.text
    # 通过链接获取视频相关信息
    list=biliUrl.split('/')
    BV_ID=list[4]
    new_list=list[5].split('=')
    spm_id_from=new_list[1].split('&')[0]
    vd_source=new_list[-1]

    # 视频标题
    title=get_viedeo_info(content)
    print(title)
    # 视频和音频的下载链接
    video_info=get_video_content(BV_ID,spm_id_from,vd_source,content)
    # 返回json格式的信息
    info={
        "title":title[0],
        "audio_url":video_info[0],
        "video_url":video_info[1]
    }
    # 下载音频资源
    save(title[0],video_info[0],video_info[1],biliheaders)
    # 音频合成
    res= merge_data(title[0])
    return res

@app.route('/api/v/kuaishou',methods=['POST'])
def kuaishouDownload():
    url=request.get_json()["data"]
    print(url)
    if not os.path.exists('./ks_video'):
        os.mkdir('./ks_video')
    if not os.path.exists('./ks_video/temp'):
        os.mkdir('./ks_video/temp')
    response=requests.get(url=url,headers=biliheaders)
    print(response.text)
    # 获取视频标题
    title=re.findall(r'class="video-info-title"[^>]*>(.*?)<a href=',response.text)
    # 获取视频播放链接
    video_url=re.findall(r'class="video-info-title"[^>]*>(.*?)></video>',response.text)
    # chinese_pattern = re.compile(r'[\u4e00-\u9fa5]')  # 匹配汉字的正则表达式
    # title=re.findall(chinese_pattern,titleStr)[0]
    return response

@app.route('/api/v/douyin',methods=['POST'])
def douyinDownload():
    url=request.get_json()["data"]
    if not os.path.exists('./dy_video'):
        os.mkdir('./dy_video')
    if not os.path.exists('./dy_video/temp'):
        os.mkdir('./dy_video/temp')
    response=requests.get(url=url,headers=dyheaders)
    data = response.json()

    # 处理获取到的视频数据
    for video in data['aweme_list']:
        video_url = video['video']['play_addr']['url_list'][0]
        # 下载视频或进行其他操作


#获取视频标题
def get_viedeo_info(content):
    #标题不能包含空格
    print(content)
    title=re.findall(r'<title data-vue-meta="true">(.*?)_哔哩哔哩bilibili</title>',content)[0].replace(' ','')
    # </script> <title data-vue-meta="true">6分钟连送6个头，德华海月惊艳众人_哔哩哔哩bilibili</title>
    video_info=[title]
    return video_info

#获取视频的视频和音频的链接
def get_video_content(BV_ID,spm_id_from,vd_source,content):
    # window.__playinfo__ =({.*?})
    #(.*?只能匹配字符不能匹配符号,例如'{}')
    json_data=re.findall(r'window\.__playinfo__=({.*?})\s*</script>',content)[0]
    #json字符串转换为python对象
    data=json.loads(json_data)
    audio_url=data['data']['dash']['audio'][0]['baseUrl']
    video_url=data['data']['dash']['video'][0]['baseUrl']
    video_content=[audio_url,video_url]
    return video_content


#数据保存
def save(title,audio_url,video_url,headers):
    audio_content=requests.get(url=audio_url,headers=headers).content
    video_content =requests.get(url=video_url,headers=headers).content
    with open('b_video\\temp\\'+title + '.mp4', mode='wb') as v:  
        v.write(video_content)  
    print(title + '.mp4', '保存完成')
    with open('b_video\\temp\\'+title +'.mp3', mode='wb') as a:  
        a.write(audio_content)  
    print(title + '.mp3', '保存完成')  
   
#音视频合成
def merge_data(video_name):
    # 数据合并
    cmd=f"ffmpeg -i 'b_video\\temp\\'{video_name}.mp4 -i 'b_video\\temp\\'{video_name}.mp3 -c:v copy -c:a aac -strict experimental b_video\\{video_name}.mp4"
    subprocess.run(cmd,shell=True)
        # 把图片读成二进制，返回到前端
    video = open(f"b_video\\{video_name}.mp4", mode='rb')
    response = Response(video, mimetype="video/mp4")
    # 第一次转码 file_name='%E3%80%8A520AM%E3%80%8B%E8%A1%A8%E7%99%BD%E8%88%9E'
    file_name=quote(video_name.encode('utf-8')) 
    # 第二次转码，名字存在中文问题未解决，不支持Unicode
    response.headers["Content-Disposition"] = "attachment;filename="+file_name
    response.headers['Content-Type']="application/octet-stream"
    return response

'''
# 前端路由
{ path: "/", name: 'Home', component: Home },
{ path: "/posts/:id", name: 'Details', component: Details, props: true },
{ path: "/create", name: 'Create', component: Create },
{ path: "/tags/:tag", name: 'Tag', component: Tags },
'''

# 博客内容api
# 从数据库中获取blog信息
@app.route('/api/posts', methods=['POST','GET'])
def add_get():
    article=Article()
    if request.method=='POST':
        data=request.get_data().decode('UTF-8')
        article.insert_blog(data)
        return 'submit-success'
    if request.method=='GET':
        posts=json.dumps(article.get_posts(),ensure_ascii=False)
        print(posts)
        return posts
@app.route('/api/posts/<id>', methods=['DELETE'])
def dele(id): 
    article=Article()
    article.del_blog(id)
    return 'del-success'
@app.route('/api/post/<id>', methods=['GET'])
def getpost(id): 
    article=Article()
    post=json.dumps(article.get_post(id),ensure_ascii=False)
    return post
# @app.route('/api/posts', methods=['GET','POST'])
# def index():
#     if request.method=='POST':
#         data=request.get_data()
#         print(type(data.decode('UTF-8')))
#         with open('./db.json','a',encoding = 'utf-8') as fw:
#             fw.write(data.decode('UTF-8'))
#             fw.close()
#         if data:
#             return 'submit-success'
#         else:
#             return 'submit-fail'
#     if request.method=='GET':
#         with open('./db.json','r',encoding='utf-8') as fp:
#             rdata=fp.read().replace(' ','').replace('\n','')
#             print(rdata)
#         fp.close()
#         return rdata
# # 删除博客

# # 发布博客

if __name__ == '__main__': 
    app.run()
