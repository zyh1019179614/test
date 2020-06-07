#python 3.6
# -*- coding:utf-8 -*-

__author__ = 'ZYH'

import json
import pymysql
import requests

conn = pymysql.connect(
    host='localhost',  # mysql服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='password',  # 密码
    db='finalstruct',  # 数据库名称
)
cur = conn.cursor()  # 创建并返回游标

# 根据文件内容创建表头
sql_1 = "CREATE TABLE code_frequency (week VARCHAR(100),add_num VARCHAR(100),def_num VARCHAR(100));"
# cur.execute(sql_1) #执行上述sql命令，首次运行时，需要执行上面的语句，用于创建table

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = 'https://api.github.com/repos/elastic/elasticsearch/stats/code_frequency'

try:
    # r = requests.get(url, headers = headers)
    # print("Status Code:", r.status_code)
    # s = json.loads(r.content)
    # filename = 'code_frequency.json'
    # with open(filename, 'w') as file_obj:
    #     json.dump(s, file_obj)

    s = open("code_frequency.json", "r")
    out = s.read()
    tmp = json.dumps(out)
    tmp = json.loads(out)
    x = len(tmp)
    # print(tmp)
    # print(x)
    i = 0
    while i < x:
        M = tmp[i]
        # print(H[0])
        sql_2 = "insert into code_frequency (week,add_num,def_num) values (" + "'"+str(M[0])+"'" +"," + "'"+str(M[1])+"'" +"," + "'"+str(M[2])+"'" +");"
        print(sql_2)
        cur.execute(sql_2)  # 执行上述sql命令
        conn.commit()
        i = i+1
    conn.close()
except Exception as e:
    print(e)
