import numpy as np
import sys
from ai_graph import AIGraph
from extra import Graph_Problem, multi_g, h
from search import best_first_graph_search


# create graph and store data in different format
graph = AIGraph(sys.argv[1])
graph.store_table()
graph.store_h()

# create graph problem
problem = Graph_Problem(graph.S, graph.G, graph.filename)

# search
sol_node = best_first_graph_search(problem, h)

# grab data desired in printing
sol_nodes = np.empty(len(sol_node.path()))
for i, node in enumerate(sol_node.path()):
    sol_nodes[i] = node.state
path_cost = multi_g(graph, sol_nodes.astype(int))

# output solution data as string
s = '\n'
for i in range(len(path_cost)):
    if i < len(path_cost) - 1:
        s += '{} - [{}] -> '.format(int(sol_nodes[i]), int(path_cost[i+1] - path_cost[i]))
    else:
        s += '{}\n'.format(int(sol_nodes[i]))

s += 'Total Path Cost: {}'.format(int(path_cost[-1]))

print(s)
