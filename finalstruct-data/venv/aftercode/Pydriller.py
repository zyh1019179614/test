from pydriller import  RepositoryMining
import json
from tqdm import tqdm

author_dict = dict()
for commit in tqdm(RepositoryMining('F:\GitHub\elasticsearch').traverse_commits()):
    if commit.author.email not in author_dict:
        author_dict[commit.author.email] = dict()
        author_dict[commit.author.email]['name'] = str(commit.author.name)
        author_dict[commit.author.email]['cmt'] = 0
        author_dict[commit.author.email]['add'] = 0
        author_dict[commit.author.email]['del'] = 0
        author_dict[commit.author.email]['fixes'] = 0
        author_dict[commit.author.email]['files'] = 0
    author_dict[commit.author.email]['cmt'] += 1
    if 'fix' in commit.msg:
        author_dict[commit.author.email]['fixes'] += 1
    for mod in commit.modifications:
        author_dict[commit.author.email]['add'] += mod.added
        author_dict[commit.author.email]['del'] += mod.removed
        author_dict[commit.author.email]['files'] += 1

filename = 'Pydriller.json'
with open(filename, 'w') as file_obj:
    json.dump(author_dict, file_obj)



