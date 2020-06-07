#python 3.6
# -*- coding:utf-8 -*-

__author__ = 'ZYH'

import json
import requests
from tqdm import tqdm

# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url = 'https://api.github.com/repos/elastic/elasticsearch/pulls/comments?per_page=100&page={}'
# total_page = 1053
# total_data = []
#
# for page in tqdm(range(1,total_page)):
#     try:
#         r = requests.get(url.format(page), headers=headers)
#         print("Status Code:", r.status_code)
#         s = json.loads(r.content)
#         total_data.extend(s)
#     except Exception as e:
#         print(e)
# filename = 'pr_comment.json'
# with open(filename, 'w') as file_obj:
#     json.dump(total_data, file_obj)

pulls_comment_dict = dict()
pulls_comments = json.load(open("pr_comment.json", "r"))

for pulls_comment in pulls_comments:
    if not isinstance(pulls_comment,dict):
        continue
    pulls_comment_dict[pulls_comment['user']['login']] = dict()
    pulls_comment_dict[pulls_comment['user']['login']]['name'] = pulls_comment['user']['login']

filename = 'pr_comments.json'
with open(filename, 'w') as file_obj:
    json.dump(pulls_comment_dict, file_obj)