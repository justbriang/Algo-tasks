import os

import networkx as nx
import matplotlib.pyplot as plt



from classes.greedbfs import GBfsTraverser

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","Phase3","J1","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",label=" 450" ,distance=450)
G.add_edge("Siwaka","Ph.1A",label="10",distance=10)
G.add_edge("Siwaka","Ph.1B",label="230" ,distance=230)
G.add_edge("Ph.1A","Ph.1B",label="100" ,distance=100)
G.add_edge("Ph.1A","Mada",label="850" ,distance=850)
G.add_edge("Ph.1B","Phase2",label="112", distance=112)
G.add_edge("Ph.1B","STC",label="50" ,distance=50)
G.add_edge("STC","Phase2",label="50", distance=50)
G.add_edge("STC","ParkingLot",label="250",distance=250)
G.add_edge("Phase2","Phase3",label="500", distance=500)
G.add_edge("Phase3","ParkingLot",label="350", distance=350)
G.add_edge("Phase2","J1",label="600", distance=600)
G.add_edge("J1","Mada",label="200" ,distance=200)
G.add_edge("Mada","ParkingLot",label="10", distance=10)
#position the nodes to resemble Nairobis map
G.nodes["SportsComplex"]['pos']=(-12,2)
G.nodes["Siwaka"]['pos']=(-1,2)
G.nodes["Ph.1A"]['pos']=(8,2)
G.nodes["Ph.1B"]['pos']=(8,0)
G.nodes["STC"]['pos']=(8,-1)
G.nodes["Phase2"]['pos']=(12,0)
G.nodes["J1"]['pos']=(18,0)
G.nodes["Mada"]['pos']=(24,0)
G.nodes["Phase3"]['pos']=(18,-1)
G.nodes["ParkingLot"]['pos']=(18,-2)
#store all positions in a variable

def getHeuristics(G):
    heuristics = {}
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, 'heuristics.txt'))
    for i in G.nodes():
        node_heuristic_val = f.readline().split()
        heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
    return heuristics


heuristics = getHeuristics(G)
node_pos = nx.get_node_attributes(G,'pos')

#call BFS to return set of all possible routes to the goal
route_bfs = GBfsTraverser()
routes = route_bfs.GBFS(G,heuristics,"SportsComplex","ParkingLot")


route_list = route_bfs.path
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_label=nx.get_edge_attributes(G,'label')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=5,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_label)
plt.axis('off')
plt.show()