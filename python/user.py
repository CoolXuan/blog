from pymysql import NULL, connect
from flask import jsonify
import random

class User(object):
    def __init__(self):  # 创建对象的同时执行代码
        print('数据库')
        self.conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            database='cx',
            password='123456'
        )
        self.cursor = self.conn.cursor()

    def __del__(self):  # 释放对象的同时执行代码
        print('释放')
        self.cursor.close()
        self.conn.close()

    def get_data(self,email): 
        sql = "select * from user where email like "+"'"+email+"%'"
        self.cursor.execute(sql)
        data = []
        for item in self.cursor.fetchall():
            data.append(item)
        if data == []:
            print('此账号未注册！')
        self.conn.commit()
        # print(3,data[0][2])
        return data

    def insert_data(self, email, password):
      # 系统自动随机分配sid
        sid = str(int(random.random()*100000))
        UserName = '无名小卒'+str(int(random.random()*1000000))
        sql = 'INSERT INTO User(sid,Email,UserName,Password,ImgUrl)VALUES(' + \
            sid+',"'+email+'","'+UserName+'","'+password+'","null");'
        self.cursor.execute(sql)
        self.conn.commit()
        return UserName
