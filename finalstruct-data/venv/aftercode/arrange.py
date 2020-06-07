__author__ = 'ZYH'

import json
import requests
import csv
import pandas as pd

# author_driller = json.load(open("Pydriller.json", "r"))
#
# with open('pydriller.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name','cmt','add','del','fixes','files']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for _, author in author_driller.items():
#         try:
#             writer.writerow(author)
#         except Exception as e:
#             continue

pydriller = pd.read_csv('pydriller.csv',encoding='gbk')
aftercode = pd.read_csv('aftercode.csv',encoding='gbk')

arran=pd.merge(pydriller,aftercode,on='name',how='left')
arran.to_csv('arrange.csv',encoding='gbk')