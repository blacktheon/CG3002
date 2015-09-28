import heapq
import json
import urllib
import math
import path
import locate

INF = 1000000000
NLINE = "==============================================="
debugMode = 1

building = raw_input("pleaes enter building name: ")
level = raw_input("pleaes enter the level number: ")

if debugMode == 1:
    print NLINE
    print "Start loading the map and parsing information"
    print NLINE

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
        orientation = int(data[i]);
        #print "orientation is: " + str(orientation)
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

if debugMode == 1:
    print "V = " + str(V)
    print "E = " + str(E)

map_cor = [[0, 0] for x in range(V+1)]

for x in raw_map:
    map_cor[int(x[2])] = [int(x[0]), int(x[1]), x[3]]

if debugMode == 1:
    #print all coordinate
    print "Here are all the nodes in the giving map"
    for i in range(1, len(map_cor)):
        print map_cor[i]


AdjList = [[] for x in range(V+1)]

for x in raw_map:
    u = int(x[2]) # ID
    for y in x[4]:
        v = int(y)
        w = math.sqrt((map_cor[u][0] - map_cor[v][0]) ** 2 + (map_cor[u][1] - map_cor[v][1]) ** 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        AdjList[u].append([v, w])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

if debugMode == 1:
    print NLINE
    print "Here are all the edges in the giving map" 
    #print all edges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    for i in range(1, V+1):
        print AdjList[i]
    print NLINE

source = int(raw_input("pleaes enter the source Vertex: "))
destination = int(raw_input("pleaes enter the destination Vertex: "))

if debugMode == 1:
    print NLINE
    print "Culculating the path"
    print NLINE

mypath = path.findPath(V, E, map_cor, AdjList, source, destination)
print "The path we found is"
print mypath

if debugMode == 1:
    print NLINE

cur_x = int(raw_input("pleaes enter the current x coordinate: "))
cur_y = int(raw_input("pleaes enter the current y coordinate: "))
heading = int(raw_input("pleaes enter the current direction: "))

if debugMode == 1:
    print NLINE
    print "Culculating the nearest node"
    print NLINE

result = locate.locationFinding(V, E, orientation, cur_x, cur_y, heading, map_cor)

map_heading = result[0]
angle = result[1]
turning = result[2]
LR = result[3]
nearest = result[4]

if debugMode == 1:
    print "The user's heading in map is: " + str(map_heading)
    print "The direction of nearest node from current position is: " + str(angle)
print "The user shall turn " + str(turning) + " degrees to the " + LR
print "Next node is in distance of " + str(nearest[0]) + " centimeters"

if debugMode == 1:
    print NLINE
    print "Culculating the new path"
    print NLINE

mypath = path.findPath(V, E, map_cor, AdjList, nearest[1], destination)
print "The new path we found is"
print mypath


