import networkx as nx
import matplotlib.pyplot as plt


from classes.ucs import Ucs

G = nx.Graph()
nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "Phase2", "STC", "Phase3", "J1", "Mada", "ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()  # confirm nodes

# Add Edges and their weights
G.add_edge("SportsComplex", "Siwaka", weight=450)
G.add_edge("Siwaka", "Ph.1A", weight=10)
G.add_edge("Siwaka", "Ph.1B", weight=230)
G.add_edge("Ph.1A", "Ph.1B", weight=100)
G.add_edge("Ph.1A", "Mada", weight=850)
G.add_edge("Ph.1B", "Phase2", weight=112)
G.add_edge("Ph.1B", "STC", weight=50)
G.add_edge("STC", "Phase2", weight=50)
G.add_edge("STC", "ParkingLot", weight=250)
G.add_edge("Phase2", "Phase3", weight=500)
G.add_edge("Phase3", "ParkingLot", weight=350)
G.add_edge("Phase2", "J1", weight=600)
G.add_edge("J1", "Mada", weight=200)
G.add_edge("Mada", "ParkingLot", weight=700)

# position the nodes to resemble Nairobis map
G.add_node("SportsComplex", pos=(-12, 2), heuristic=730)
G.add_node("Siwaka", pos=(-1, 2), heuristic=405)
G.add_node("Ph.1A", pos=(8, 2), heuristic=380)
G.add_node("Ph.1B", pos=(8, 0), heuristic=280)
G.add_node("STC", pos=(8, -1), heuristic=213)
G.add_node("Phase2", pos=(12, 0), heuristic=210)
G.add_node("J1", pos=(18, 0), heuristic=500)
G.add_node("Mada", pos=(24, 0), heuristic=630)
G.add_node("Phase3", pos=(18, -1), heuristic=160)
G.add_node("ParkingLot", pos=(18, -2), heuristic=0)

# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')

# call BFS to return set of all possible routes to the goal
route_gbfs = Ucs()
routes = route_gbfs.ucs(G, "SportsComplex", "STC")
print(route_gbfs.visited)
route_list = route_gbfs.visited

# color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list, route_list[1:]))

# color the edges as well
# print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
# nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
