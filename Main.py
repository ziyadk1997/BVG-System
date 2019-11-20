# All single character variables are indexes
# Reading the data of the stations from a text file
import os.path
import time
stationsTextFile = open(os.path.dirname(__file__)+"/Stations.txt", "r")
uBahnData = stationsTextFile.read()
stationsLatLangFile = open(os.path.dirname(__file__)+"/AllStationsLatLang.txt", "r")
stationsLatLang = stationsLatLangFile.read().split("\n")
latList = []
longList = []
for line in stationsLatLang:
	if line == "":
		break
	lineSplited = line.split(",")
	latList.append(float(lineSplited[1]))
	longList.append(float(lineSplited[2]))
R = 6373.0
# Imports
from collections import defaultdict
from math import sin, cos, sqrt, atan2, radians

# This class represents a Node Object
class Node(object):
    #constructor
    def __init__(self,ID):
        self.visited = False
        self.heuristic = 0.0
        self.parentNode = None
        self.possibleMoves = []
        self.Us = []
        self.possibleMovesCost = []
        self.id = ID
# Graph Class has default dict of Nodes and the Traversals
class Graph: 

	# Constructor 
	def __init__(self): 
		# default dictionary to store graph 
		self.graph = defaultdict(Node) 
  #BFS Traversal 
	def BFS(self,startNode,goalNode): 
		startTimeBFS = time.time()
		expandedNodes= 0
		# Create a queue for BFS 
		queue = [] 
		#enqueue first startNode to start traversing BFS
		self.graph[startNode].visited = True
		queue.append(startNode)
		# Initialize goal Node
		goal = Node(-1)
        # traversing the queue until its empty
		while queue: 
			expandedNodes+=1
			# Dequeue an element
			currentNode = queue.pop(0)
			# check if it is a goal if it is break from the loop goal found
			if int(goalNode) == int(currentNode):
				goal = self.graph[currentNode]
				break
			# Get possible Moves for current Node
			possibleMovesArray = self.graph[currentNode].possibleMoves
			#Enqueue every possible move if not visited before
			for possibleMove in possibleMovesArray:
				if self.graph[possibleMove].visited == False: 
					self.graph[possibleMove].parentNode = self.graph[currentNode]
					queue.append(possibleMove) 
					self.graph[possibleMove].visited = True
		#If Goal Found
		if not(goal.id ==-1):
			path = []
			#Tranverse Parents of Goal Node till start Node is reached and print path
			while not (goal is None):
				#print(goal.id)
				path.insert(0,goal)
				goal = goal.parentNode
			currentUbahnLine = path[0].Us[0]
			drive1 = path[0].id
			drive2 = path[0].id
			costOfTrip = 0
			for i in range(0,len(path)-1):
				if(path[i+1].Us.__contains__(currentUbahnLine)):
					costOfTrip+=path[i].possibleMovesCost[path[i].possibleMoves.index(path[i+1].id)]
					drive2 = path[i+1].id
					if i == len(path)-2:
						if currentUbahnLine == 10:
							currentUbahnLine= 55
						print("Ride U"+str(currentUbahnLine)+" from : "+str(allStations[drive1]+" to : "+ str(allStations[drive2])))
				else:
					costOfTrip +=5
					print("Ride U"+str(currentUbahnLine)+" from : "+str(allStations[drive1]+" to : "+ str(allStations[drive2])))
					drive1 = drive2
					drive2 = path[i+1].id
					commonUbahnLine = set(path[i].Us).intersection(path[i+1].Us).pop()
					print("Switch from U"+str(currentUbahnLine)+" To U"+str(commonUbahnLine))
					currentUbahnLine = commonUbahnLine
			print("Cost of Trip is :" + str(costOfTrip))
		print("BFS searching time is "+ str(time.time()-startTimeBFS))
		print("Expanded Nodes : " + str(expandedNodes))


			

#Initialize An Array That has all stations (unique) 
allStations = []
#Remove \n from File and put each line in an element in an array
uBahnData = uBahnData.replace("\n","")
linesSeperated = uBahnData.split("#")
#Fill all Stations (each station only occuring once)
for line in linesSeperated:
	lineSeperated = line.split(",")
	for x in range (0,len(lineSeperated)-1,2):
         if not(allStations.__contains__(lineSeperated[x])):
             allStations.append(lineSeperated[x])
startTimeGraph = time.time()
#Create Graph
g = Graph()
#Add Edges with cost from each station to station
for j in range(0,len(allStations)):
	station = allStations[j]
	stationNode = Node(j)
	for line in linesSeperated:
		lineSeperated = line.split(",")
		for x in range (0,len(lineSeperated)):
			if lineSeperated[x] == station:
				stationNode.Us.append(linesSeperated.index(line)+1)
				if (x + 3) < (len(lineSeperated)) and not (stationNode.possibleMoves.__contains__(allStations.index(lineSeperated[x+2]))): 
					cost = int(lineSeperated[x+3]) - int(lineSeperated[x+1])
					stationNode.possibleMoves.append(allStations.index(lineSeperated[x+2]))
					stationNode.possibleMovesCost.append(abs(cost))
				if x > 1 and x+1 < (len(lineSeperated)) and not (stationNode.possibleMoves.__contains__(allStations.index(lineSeperated[x-2]))):
					cost = int(lineSeperated[x-1]) - int(lineSeperated[x+1])
					stationNode.possibleMoves.append(allStations.index(lineSeperated[x-2]))
					stationNode.possibleMovesCost.append(abs(cost))
	g.graph[j] = stationNode
print("Creating Graph Time is " + str(time.time()-startTimeGraph))
#DEBUGGING
g.BFS(76,137)
