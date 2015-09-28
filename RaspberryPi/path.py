import heapq
import json
import urllib
import math

INF = 1000000000

def findPath(V, E, map_cor, AdjList, source, destination):
    dist = []
    for i in range(V+1):
        dist.append(INF)
    dist[source] = 0

    lastNode = []
    for i in range(V+1):
        lastNode.append(i)

    h = []
    heapq.heappush(h, (0, source))

    while h != []:
        front = heapq.heappop(h)
        d = front[0]
        u = front[1]
        if d <= dist[u]:
            for j in range(len(AdjList[u])):
                v = AdjList[u][j]
                if (dist[u] + v[1]) < dist[v[0]]:
                    lastNode[v[0]] = u
                    dist[v[0]] = dist[u] + v[1]
                    heapq.heappush(h, (dist[v[0]], v[0]))

    #print all SSSP
    #for i in range(V+1):
    #    print "SSSP (" + str(source) + ", " + str(i) +") = " + str(dist[i])
    #    print "last node is: " + str(lastNode[i])

    curPos = destination
    inverPath = []
    inverPath.append(curPos)
    while curPos != source:
        curPos = lastNode[curPos]
        inverPath.append(curPos)

    myPath = [0 for x in range(len(inverPath))]
    for i in range(len(inverPath)):
        myPath[len(inverPath)-1 - i] = inverPath[i]
    #print the path
    return myPath







