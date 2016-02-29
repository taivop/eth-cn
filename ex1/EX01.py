from igraph import *
import numpy as np


# Task 2.1
g1 = Graph()
g1.add_vertices(3)
g1.add_edges([(0,1), (1,2), (2,0)])

summary(g1)


# Task 2.2
g2 = Graph()
g2.add_vertices(100)
for i in range(0, 200):
    edge = np.random.choice(range(0, 100), size=(2), replace=False)
    g2.add_edge(edge[0], edge[1])
    
summary(g2)    


# Task 3.1
g3 = Graph.Read_Ncol("data/EX01_gentoo_810_30d.txt")

summary(g3)

# Task 3.2
layout = g3.layout_fruchterman_reingold()
plot(g3, layout = layout)
visual_style = {}
visual_style["vertex_size"] = 5
visual_style["vertex_color"] = "red"
visual_style["label_size"] = 6
visual_style["vertex_label"] = g3.vs["name"]
visual_style["arrow_size"] = 0.2

# Task 3.3
plot(g3, "output/network_g3.pdf", **visual_style)