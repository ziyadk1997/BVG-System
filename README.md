# BVG-System
This is a project for GUC AI Course the aim of the project is to create a BVG like system that find a path from one station to another using 3 different searching Algorithms we choose DFS and BFS for the 2 Uninformed searches and greedy algorithm for the informed the heuristic function was calculated using the latitude and longitude of the stations (straight line path).

Collaborators :
Ziyad Khaled 37-9052
Mohamed Ashraf Lotfy 37-4455
Omar Khaled Rifky 37-538

The Code reads from 2 files one contains 10 Ubahn Lines and the other contains the latLong of each Station There are 2 classes Class Node and Class Graph the node defines each station when entered into the graph and its attributes the Graph itself is using a defaultdict of Nodes.

The greedy uses a list to traverse the graph always removing node with lowest heuristic function.The BFS uses a queue to tranverse removing the first in. The DFS uses a stack to traverse removing last in.

To run code g is the graph can use g.DFS(start,end) or g.BFS(start,end) or g.Greedy(start,end).
start and end in the function are integers use file StopNames.txt for Reference.