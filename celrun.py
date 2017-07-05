
#!/usr/bin/python
import beggar
import worker

start = 142153421643
trials = 10
d = beggar.GameNo(start=start)

while(trials > 0):
	trials -= 1
	gameno = d.next()
	worker.Search.delay(gameno)
	#print "{}".format(Search(gameno))


#try:
#    from numpy import histogram
#    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
#    for (v,b) in zip(hist, [int(i) for i in bins]):
#        print "{0},{1}".format(b,v) 
#except ImportError:
#    print "No Numpy module"
