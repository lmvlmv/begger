#!/usr/bin/python
import beggar
import time
import sys
import os

from celery import Celery

broker = os.environ['BROKER_URI']
app = Celery('worker', backend='rpc://', broker=broker )

@app.task
def add(x, y):
	return x + y

@app.task
def Search(gameno):
	deal = beggar.Deal(gameno)
	cont = True
	maxturns = 0
	while(cont):
	    try:
			(left, right) = deal.next()
			(turns, tricks, starts) = beggar.play((left,right),verbose=False)
			if turns > maxturns:
				maxturns = turns
	    except StopIteration:
			cont = False
	return maxturns

