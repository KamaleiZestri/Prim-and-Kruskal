# -*- coding: utf-8 -*-
import re
from Weighted_Graph import Weighted_Graph as wg

def generateIncidentEdges(graph,tree):
    #Takes two Weighted Graph operands. Generates all incident edges of 2nd based on 1st.
    #If 2nd tree is empty, random vertex from 1st is used as beginning. 
    #Returns a Weighted Graph object that includes the incident edges.
    incidentEdges=wg.Weighted_Graph()
    if(not tree.vertex_list()):
        i=graph.vertex_list()[0]
        for k in graph.edge_list():
                edge= re.findall("'([0-9)*])'",str(k))
                for j in edge:
                    if(j == i):
                        if(k not in tree.edge_list()):
                            incidentEdges.add_edge(k,graph.get_weight(k))
    else:
        for i in tree.vertex_list():
            for k in graph.edge_list():
                edge= re.findall("[0-9]",str(k))
                for j in edge:
                    if(j==i):
                        if(k not in tree.edge_list()):
                            incidentEdges.add_edge(k,graph.get_weight(k))
    return incidentEdges        
                    
        
def checkIsTree(incidentEdges,tree):
    #Takes two Weighted Graph operands. Every edge in the 1st is added to the 2nd temporarily to see
    #if the edge causes the 2nd to cycle.
    #Returns a list of edges that will not cause the tree to cycle
    temp=wg.Weighted_Graph()
    for i in incidentEdges.edge_list():
        temp.add_edge(i,incidentEdges.get_weight(i))
        
    for k in incidentEdges.edge_list():
        tree.add_edge(k,incidentEdges.get_weight(k))
        if(len(tree.edge_list())!=len(tree.vertex_list())-1):
            temp.remove_edge(k)
        tree.remove_edge(k)
    return temp
    
def findMinimumEdge(incidentEdges):
    #Takes on Weighted Graph operand. Returns the first edge that has the least weight.
    minkey=incidentEdges.edge_list()[0]
    for i in incidentEdges.edge_list():
        if(incidentEdges.get_weight(i)<incidentEdges.get_weight(minkey)):
            minkey=i
    return minkey