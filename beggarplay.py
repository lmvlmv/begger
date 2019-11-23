
from celery import Celery
from beggar import Player

app = Celery('beggarplay', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def play(court, hands):
    return Player(court, hands).play()