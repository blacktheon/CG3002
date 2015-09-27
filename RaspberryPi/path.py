import heapq
import json
import urllib
import math

INF = 1000000000

building = raw_input("pleaes enter building name: ")
level = raw_input("pleaes enter the level number: ")
url_head = "http://ShowMyWay.comp.nus.edu.sg/getMapInfo.php?Building="
url = url_head + building + "&Level=" + level

response = urllib.urlopen(url)
#text = json.loads(response.read())
text = json.load(response)
#print text

data = str(text).split('u\'')
#print data

for i in range(len(data)):
    data[i] = str(data[i]).split('\'')[0]
#print data

i = 0
mode = 'INIT'
raw_map = []
V = 0
E = 0
while i < len(data):
    if data[i] == 'northAt':
        mode = 'ORI'
    elif data[i] == 'map':
        mode = 'MAP'
    elif data[i] == 'wifi':
        mode = 'WIFI'

    if mode == 'ORI':
        i = i+1
        orientation = data[i];
        print "orientation is: " + orientation
        i = i+1
    elif mode == 'MAP':
        if data[i] == 'y':
            y_cor = data[i+1]
        elif data[i] == 'x':
            x_cor = data[i+1]
        elif data[i] == 'nodeId':
            ID = data[i+1]
        elif data[i] == 'linkTo':
            links = str(data[i+1]).split(', ')
        elif data[i] == 'nodeName':
            name = data[i+1]
            raw_map.append([x_cor, y_cor, ID, name, links])
            #print "node " + ID + ": " + name + " (" + x_cor + ", " + y_cor + ") connected to: "
            for x in links:
                #print x
                E = E + 1
            V = V + 1
        i = i+1
    elif mode == 'WIFI':
        i = len(data)  #terminate for now because we dont need
    else: # mode not started
        i = i+1
print "V = " + str(V)
print "E = " + str(E)
map_cor = [[0, 0] for x in range(V+1)]

for x in raw_map:
    map_cor[int(x[2])] = [int(x[0]), int(x[1]), x[3]]
for x in map_cor:
    print x

AdjList = [[] for x in range(V+1)]

for x in raw_map:
    u = int(x[2]) # ID
    for y in x[4]:
        v = int(y)
        w = math.sqrt((map_cor[u][0] - map_cor[v][0]) ** 2 + (map_cor[u][1] - map_cor[v][1]) ** 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        AdjList[u].append([v, w])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
for i in range(V+1):
    print AdjList[i]


source = int(raw_input("pleaes enter the source Vertex: "))
destination = int(raw_input("pleaes enter the destination Vertex: "))

dist = []
for i in range(V+1):
    dist.append(INF)
dist[source] = 0

lastNode = []
for i in range(V+1):
    lastNode.append(i)

print lastNode

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

for i in range(V+1):
    print "SSSP (" + str(source) + ", " + str(i) +") = " + str(dist[i])
    print "last node is: " + str(lastNode[i])

curPos = destination
inverPath = []
inverPath.append(curPos)
while curPos != source:
    curPos = lastNode[curPos]
    inverPath.append(curPos)

myPath = [0 for x in range(len(inverPath))]
for i in range(len(inverPath)):
    myPath[len(inverPath)-1 - i] = inverPath[i]
print myPath










