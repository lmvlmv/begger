
#!/usr/bin/python
import beggar
import worker
from celery.result import ResultSet

start = 343685886
trials = 4

d = beggar.GameNo(start=start)
rs = ResultSet([])

while(trials > 0):
	trials -= 1
	gameno = d.next()
	rs.add(worker.Search.delay(gameno))
	#print "{}".format(Search(gameno))

print max(rs.join())

#try:
#    from numpy import histogram
#    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
#    for (v,b) in zip(hist, [int(i) for i in bins]):
#        print "{0},{1}".format(b,v) 
#except ImportError:
#    print "No Numpy module"
