# Randomized Contraction - Karger Min-Cut Algorithm.


#The graph is undirected and has 200 nodes(vertices) with edges inbetween.

#Steps
# 1. Read the file.
# 2. Make a graph.
# 3. Contract and count the min-cut.


import random
from random import choice
import math

#Make a dictionary to represent graph.
graph={}

# Reads the file and creates a graph, represented as dictionary. 
# (ie) {node:[node1,node2]}
# eg) {1: [37, 79, 164, 155, 32, 87, 39, 113, 15, 18, 78, 175, 140, 200, 4, 160, 97, 191, 100, 91, 20, 69, 198, 196], 2: [123, 134, 10, 141, 13, 12, 43, 47, 3, 177, 101, 179, 77, 182, 117, 116, 36, 103, 51, 154, 162, 128, 30]...}
def read_file(file_name):
    file_open=open(file_name,'r')
    lines=file_open.readlines()
    for line in lines:
        line=list(map(int,line.split()))
        #print(line)
        #graph[line[0]]=[] 
        graph[line[0]]=line[1:] #append(line[1:]) <-- this will make a list inside a list which we do not want.
    file_open.close()     
    return graph

#Get a random edge.
def get_random_edge():
    v1 = list(graph)

    v1=v1[random.randint(0,len(graph)-1)]

    v2 =graph[v1][random.randint(0,len(graph[v1])-1)]   

    
    #Alternate way to use choice
    #v1 = choice(list(graph.keys()))
    #v2 = choice(graph[v1])
    return (v1,v2)


#Contract node v1 and v2 such that v1<----v2
#As v2 is contracted into v1, remove v2 node from the graph
def contract(v1,v2):
    for node in graph[v2]:
        #check if it a self loop node
        if node!=v1:
            #add node to v1 adjacency list
            graph[v1].append(node)
            #add v1 to node adjaceny list
            graph[node].append(v1) 
            #Remove v2 from node adjacency list 

        if v2 in graph[node]: 
            graph[node].remove(v2) 
    #Remove v2 from the graph
    del graph[v2]



#-------------------------
# Karger Min-cut Algorithm

read_file('kargerMinCut.txt')
#Test the functions
#print(graph)
#print(get_random_edge())

cut=[]
print("graph length",len(graph))
num_vertices=len(graph)

#probability of success is 1/n when number of trials is nc2*ln(n)
trials=int(num_vertices*(num_vertices-1)*math.log(num_vertices)/2)
print("trials for success probability (1/n)",trials)

#probability of success is 1/e when number of trials is n*n
trials=num_vertices*num_vertices 
print("trials for success probability (1/e)",trials)

#choose trials to be 100, ( for reducing the program running time) , 
#The total running time for T repetitions for a graph with vertices and m edges is O ( T m ) = O ( n^2 m log ⁡ n ) ~ Big Omega(n^2 m) [lower bound]
trials=100


for i in range(1,trials):
    read_file('kargerMinCut.txt')
    
    #Loop until 1 edge (ie) 2 nodes remain.
    while len(graph)>2:
        v1,v2=get_random_edge()
        contract(v1,v2)

    #Mincut is the count of the nodes in the adjacency list (ie) edges.
    #Graph now has 2 nodes in its adjacency list. 
    mincut = len(graph[list(graph.keys())[0]])
    #mincut2= len(graph[list(graph.keys())[1]])
    #print("trial",i,"mincut",mincut,"mincut2",mincut2)

    #Add to the min-cut list.
    cut.append(mincut)

#Min-cut is the minimum in the cut list.
print("mincut",min(cut))


