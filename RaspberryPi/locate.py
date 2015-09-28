import heapq
import math

def locationFinding(V, E, orientation, cur_x, cur_y, heading, map_cor):
    map_heading = heading + orientation
    if map_heading > 360:
        map_heading = map_heading%360

    distpq = []
    for i in range(1, V+1):
        heapq.heappush(distpq, (math.sqrt((map_cor[i][0] - cur_x) ** 2 + (map_cor[i][1] - cur_y) ** 2), i))
    nearest = heapq.heappop(distpq)
    print "The nearest node is: Node " + str(nearest[1])

    x1 = map_cor[nearest[1]][0]
    y1 = map_cor[nearest[1]][1]
    a = x1 - cur_x
    b = y1 - cur_y
    cosA = a/(math.sqrt(a ** 2 + b ** 2))
    angle = (math.acos(cosA) / math.pi) * 180
    if a >= 0:
        if b >= 0:
            angle = angle
        elif b < 0:
            angle = 180 - angle
    elif a < 0:
        if b <= 0:
            angle = 180 + angle
        elif b > 0:
            angle = 360 - angle

    turning = abs(angle - map_heading)
    if angle >= map_heading:
        LR = "right"
    else:
        LR = "left"

    result = []
    result.append(map_heading)
    result.append(angle)
    result.append(turning)
    result.append(LR)
    result.append(nearest)

    return result