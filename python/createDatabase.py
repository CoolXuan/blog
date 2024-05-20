import pymysql

DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = '123456'
DBNAME = 'cx'
initData = ['1', '1976756410@qq.com','root', '123456', '1', '2023-2-4      11:10:33', '2023-2-4      11:10:33']
create = True
try:
    # 数据库链接
    db = pymysql.connect(host=DBHOST, user=DBUSER,
                         password=DBPASS, database=DBNAME)
    print('数据库成功连接')
    cur = db.cursor()
    # # 创建表格
    if create==True:
        sql = 'CREATE TABLE user(userId char(50),email VARCHAR(50),username VARCHAR(50),password VARCHAR(50),isVip CHAR(50),currentTime CHAR(50),loginTime CHAR(50))'
        cur.execute(sql)
    # 插入数据
    sql = 'INSERT INTO user(userId,email,username,password,isVip,currentTime,loginTime)VALUE(%s,%s,%s,%s,%s,%s,%s)'
    # for data in initData:
    value = tuple(initData)
    cur.execute('alter database cx character set utf8;')
    cur.execute(sql, initData)
    db.commit()
    print("表格创建成功")
    # 向表格插入一条数据
except pymysql.Error as e:
    print('数据库连接失败')
    print(e)
    db.rollback()
# 关闭数据库
db.close()
