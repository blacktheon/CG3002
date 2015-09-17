import sys
for a in sys.path:
	print a

spath="test.txt"
f=open(spath,"w")
f.write("First line 1.\n")
f.writelines("First line 2.")
f.close()

f=open(spath, "r")
for line in f:
	print line
f.close()

#pq=[]
#heappush(pq, (4, 3))
#heappush(pq, (5, 2))
#heappush(pq, (6, 1))
#heappop(pq)
