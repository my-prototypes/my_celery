from celery import Celery
import subprocess

app = Celery('tasks', backend='amqp')

@app.task
def clone_repository(repo_url):
    subprocess.call(['git', 'clone', repo_url])