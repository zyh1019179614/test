from pydriller import  RepositoryMining,git_repository

print(git_repository.GitRepository('F:\GitHub\elasticsearch').total_commits())
