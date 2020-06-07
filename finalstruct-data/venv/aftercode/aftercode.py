#python 3.6
# -*- coding:utf-8 -*-

__author__ = 'ZYH'

import json
import requests
import csv

author_dict = dict()

issues = json.load(open("issues.json", "r"))
issues_comments = json.load(open("issues_comments.json", "r"))
pulls = json.load(open("pr.json", "r"))
pulls_comments = json.load(open("pr_comments.json", "r"))
author_driller = json.load(open("Pydriller.json", "r"))
# author_driller = {v['name']:v.update({'email':k}) for k,v in author_driller.items()}

for issue in issues:
    if issue['user']['login'] not in author_dict:
        author_dict[issue['user']['login']]= dict()
        author_dict[issue['user']['login']]['name'] = issue['user']['login']
        author_dict[issue['user']['login']]['issues'] = 0
        author_dict[issue['user']['login']]['handle_issue'] = 0
        author_dict[issue['user']['login']]['pr'] = 0
        author_dict[issue['user']['login']]['comments'] = 0
    author_dict[issue['user']['login']]['issues'] += 1
    if issue['state'] == 'closed' and len(issue['assignees'])>0:
        for assignee in issue['assignees']:
            if assignee['login'] not in author_dict:
                author_dict[assignee['login']]= dict()
                author_dict[assignee['login']]['name'] = assignee['login']
                author_dict[assignee['login']]['issues'] = 0
                author_dict[assignee['login']]['handle_issue'] = 0
                author_dict[assignee['login']]['pr'] = 0
                author_dict[assignee['login']]['comments'] = 0
            author_dict[assignee['login']]['handle_issue'] += 1

for pull in pulls:
    if pull['user']['login'] not in author_dict:
        author_dict[pull['user']['login']] = dict()
        author_dict[pull['user']['login']]['name'] = pull['user']['login']
        author_dict[pull['user']['login']]['pr'] = 0
        author_dict[pull['user']['login']]['issues'] = 0
        author_dict[pull['user']['login']]['handle_issue'] = 0
        author_dict[pull['user']['login']]['comments'] = 0
    author_dict[pull['user']['login']]['pr'] += 1

for issues_comment in issues_comments:
    r = issues_comment['user']['login']
    if issues_comment['user']['login'] not in author_dict:
        author_dict[issues_comment['user']['login']] = dict()
        author_dict[issues_comment['user']['login']]['name'] = issues_comment['user']['login']
        author_dict[issues_comment['user']['login']]['comments'] = 0
        author_dict[issues_comment['user']['login']]['pr'] = 0
        author_dict[issues_comment['user']['login']]['issues'] = 0
        author_dict[issues_comment['user']['login']]['handle_issue'] = 0
    author_dict[issues_comment['user']['login']]['comments'] += 1

for _,pulls_comment in pulls_comments.items():
    try:
        if pulls_comment['name'] not in author_dict:
            author_dict[pulls_comment['name']] = dict()
            author_dict[pulls_comment['name']]['name'] = pulls_comment['name']
            author_dict[pulls_comment['name']]['comments'] = 0
            author_dict[pulls_comment['name']]['pr'] = 0
            author_dict[pulls_comment['name']]['issues'] = 0
            author_dict[pulls_comment['name']]['handle_issue'] = 0
        author_dict[pulls_comment['name']]['comments'] += 1
    except Exception as e:
        continue

with open('aftercode.json', 'w') as file_obj:
    json.dump(author_dict, file_obj)

# with open('aftercode.csv','w',newline='') as csvfile:
#     fieldnames=['name','comments','pr','issues','handle_issue']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     for _,author in author_dict.items():
#         writer.writerow(author)

unmathed = {}
for author_name, author in author_driller.items():
    if author_name in author_dict:
        author.update(author_dict[name])
    else:
        unmathed.add(author_name)
print("Author unmatched number:" + str(len(unmathed)))

with open('author_merge.csv','w',newline='') as csvfile:
    fieldnames=['name','email','cmt','add','del','fixes','files','comments','pr','issues','handle_issue']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    for _,author in author_driller.items():
        writer.writerow(author)

with open('author_merge.json','w') as fout:
    json.dump(author_driller,fout)

