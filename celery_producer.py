from tasks import clone_repository

repo_url = 'https://github.com/example/repository.git'
clone_repository.delay(repo_url)
