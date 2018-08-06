import math
from itertools import permutations
def distance(n1, n2):
	x1, y1 = pointsDict[n1]
	x2, y2 = pointsDict[n2]
	return round(math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2)))

points = []
pointsDict = {}
graph = []
numPts = int(input())
for i in range(numPts):
	pts = input().split()
	pts = [float(x) for x in pts]
	points.append(pts)
	pointsDict[i] = points[i]
	graph.append([])
for i in range(len(graph)):
	for j in range(len(graph)):
		graph[i].append(distance(i,j))
#list(permutations(list(range(len(graph)))))
print(len(list(permutations(list(range(len(graph)))))))
