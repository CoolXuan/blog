from pymysql import NULL, connect
from flask import jsonify
import random
import json

class Article(object):
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

    def get_posts(self): 
        sql = "select * from article"
        self.cursor.execute(sql)
        data = []
        for item in self.cursor.fetchall():
            data.append(item)
        if data == []:
            print('没有博客数据')
        self.conn.commit()
        return data

    def insert_blog(self, blog):
        # 系统自动随机分配sid
        id=str(json.loads(blog)['id'])
        title=str(json.loads(blog)['title'])
        body=str(json.loads(blog)['body'])
        tags=",".join(json.loads(blog)['tags'])
        print(tags)
        current_time=str(json.loads(blog)['current_time'])
        author=str(json.loads(blog)['author'])
        sql = 'INSERT INTO article(id,title,body,tags,currentTime,author)VALUE(%s,%s,%s,%s,%s,%s)'
    # for data in initData:
        value = (id,title,body,tags,current_time,author)
        # self.conn.execute('alter database cx character set utf8;')
        self.cursor.execute(sql, value)
        self.conn.commit()
        return 'insert-article'
    
    def del_blog(self, id):
        sql = "delete from article where id="+id
        self.cursor.execute(sql)
        self.conn.commit()
        return 'del-success'
    
    def get_post(self,id):
        sql = "select * from article where id="+id
        self.cursor.execute(sql)
        data = []
        for item in self.cursor.fetchall():
            data.append(item)
        if data == []:
            print('没有博客数据')
        self.conn.commit()
        return data