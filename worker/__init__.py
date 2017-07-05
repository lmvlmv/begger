#!/usr/bin/python
import beggar
import time
import sys

from celery import Celery

app = Celery('iter', backend='rpc://', broker='pyamqp://guest@localhost//')

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

