# -*- coding: utf-8 -*-
from Weighted_Graph import Weighted_Graph as wg
import os
import PrimFunctions as pf

class Prim(object):
    
    def __init__(self,fileName="Example.txt"):
        os.getcwd       #Current directory
        os.chdir("..")  #Up one directory
        graph= wg.Weighted_Graph(os.path.relpath(fileName))  #the intial graph. tree will be a subset of this
        tree= wg.Weighted_Graph()                #the graph the tree will be made to fill
        
        while(len(tree.vertex_list()) != len(graph.vertex_list())):
            incidentEdges=wg.Weighted_Graph()
            incidentEdges=pf.generateIncidentEdges(graph,tree)
            incidentEdges=pf.checkIsTree(incidentEdges,tree)
            minCostEdge=pf.findMinimumEdge(incidentEdges)
            tree.add_edge(minCostEdge,graph.get_weight(minCostEdge))
            
        self.MSTree=tree
        self.origin=graph        
        
    def __str__(self):
        self.MSTree.draw_graph()
        return(str(self.MSTree))

p=Prim()
print(p)