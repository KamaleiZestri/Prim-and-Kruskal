from Prim import PrimMain as p
from Kruskal import KruskalMain as k

def Main(textfile="Example.txt",algorithm="Prim"):
    if (algorithm== "Prim"):
        mst= p.Prim(textfile);
    else:
        mst= k.Kruskal(textfile);
    
    print(mst);
    
#Main("Example.txt","Prim");