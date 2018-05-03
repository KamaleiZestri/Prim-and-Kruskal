from Weighted_Graph import Weighted_Graph as wg
import os
import KruskalFunctions as kf

class Prim(object):
    
    def __init__(self,fileName="Example.txt"):
        os.getcwd       #Current directory
        os.chdir("..")  #Up one directory
        graph= wg.Weighted_Graph(os.path.relpath(fileName))  #the intial graph. tree will be a subset of this
        tree= wg.Weighted_Graph()                #the graph the tree will be made to fill
        
        while(any(graph.edge_dict()) and tree.vertex_list() != graph.vertex_list()):
            temp=wg.Weighted_Graph();
            temp.add_edge(kf.minCostEdge(graph));
            if(kf.connectTrees(temp,graph,tree)):
                tree.add_edge;
            graph.remove_edge(temp.edge_list()[0]);
            
        self.MSTree=tree
        self.origin=graph        
        
    def __str__(self):
        self.MSTree.draw_graph()
        return(str(self.MSTree))