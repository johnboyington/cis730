import numpy as np
import sys
from ai_graph import AIGraph
from extra import Graph_Problem, multi_g
from search import iterative_deepening_search


# create graph and store data in different format
graph = AIGraph(sys.argv[1])
graph.store_table()

# create graph problem
problem = Graph_Problem(graph.S, graph.G, graph.filename)

# search
sol_node = iterative_deepening_search(problem)

# grab data desired in printing
sol_nodes = np.empty(len(sol_node.path()))
for i, node in enumerate(sol_node.path()):
    sol_nodes[i] = node.state
path_cost = multi_g(graph, sol_nodes.astype(int))

# output solution data as string
s = 'Best path found: '
sc = 'cost: {}'.format(int(path_cost[1] - path_cost[0]))
for i in range(len(path_cost)):
    if i < len(path_cost) - 1:
        s += '{} '.format(int(sol_nodes[i]))
        if i:
            sc += ' + {}'.format(int(path_cost[i+1] - path_cost[i]))
    else:
        s += '{};'.format(int(sol_nodes[i]))
        sc += ' = {}\n'.format(int(path_cost[i]))

print(s, sc)
