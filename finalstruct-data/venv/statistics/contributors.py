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
sql_1 = "CREATE TABLE contributors (author_id VARCHAR(100),total VARCHAR(100),weeks_w  VARCHAR(100),weeks_a  VARCHAR(100),weeks_d VARCHAR(100),weeks_c VARCHAR(100));"
cur.execute(sql_1)#执行上述sql命令，首次运行时，需要执行上面的语句，用于创建table

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = 'https://api.github.com/repos/elastic/elasticsearch/stats/contributors'

try:
    #  r = requests.get(url, headers = headers)
    # print("Status Code:", r.status_code)
    # s = json.loads(r.content)
    # filename = 'contributors.json'
    # with open(filename, 'w') as file_obj:
    #     json.dump(s, file_obj)

    s = open("contributors.json", "r")
    out = s.read()
    tmp = json.dumps(out)
    tmp = json.loads(out)
    x = len(tmp)
    # print(tmp)
    # print(x)
    i = 0
    while i < x:
        M = tmp[i]

        E = [M['author']['id'],M['total']]
        # print(E)
        j = len(M['weeks'])
        k = 0
        while k < j:
            F = [M['weeks'][k]['w'],M['weeks'][k]['a'],M['weeks'][k]['d'],M['weeks'][k]['c']]
            H = E + F
            # print(H[0])
            sql_2 = "insert into contributors (author_id,total,weeks_w,weeks_a,weeks_d,weeks_c) values (" + "'"+str(H[0])+"'" +","+ "'"+str(H[1])+"'" + ","+"'"+str(H[2])+"'" + ","+"'"+str(H[3])+"'" + ","+"'"+str(H[4])+"'" + ","+"'"+str(H[5])+"'" + ");"
            print(sql_2)
            cur.execute(sql_2)  # 执行上述sql命令
            k = k + 1
            conn.commit()

        print("============")
        i = i+1
    conn.close()
except Exception as e:
    print(e)
