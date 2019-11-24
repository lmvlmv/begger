
from celery import Celery
from beggar import Player
import os

# 'pyamqp://guest@localhost//'
app = Celery('beggarplay', backend='rpc://', broker=os.environ['BROKERURL'])

@app.task
def play(court, hands):
    return Player(court, hands).play()