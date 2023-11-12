from celery import Celery
from producer import clone_repository

app = Celery('tasks', backend='amqp')

@app.task
def consume_clone_request(message):
    repo_url = message.body['repo_url']
    clone_repository(repo_url)