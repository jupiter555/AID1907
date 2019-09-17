"""
创建数据库 dict
   创建数据表  words

     id    word    mean

   将单词本中的单词插入数据库
"""

import pymysql
import re

f = open('dict.txt')

# 连接数据库
db = pymysql.connect(user='root',
                     password = '123456',
                     database = 'dict',
                     charset='utf8')

# 获取游标 (操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()

# 执行语句
sql="insert into words (word,mean) values (%s,%s)"

for line in f:
    # tmp = line.split(' ',1)
    # word = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[word,mean])

    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    cur.execute(sql, tup)

try:
    db.commit()
except:
    db.rollback()

# 关闭游标
cur.close()
# 关闭数据库
db.close()

