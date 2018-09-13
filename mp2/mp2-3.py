import numpy as np
import sys
from ai_graph import AIGraph
from code import Graph_Problem, multi_g
from search import uniform_cost_search

graph = AIGraph(sys.argv[1])
graph.store_table()
problem = Graph_Problem(graph.S, graph.G, graph.filename)
sol_node = uniform_cost_search(problem)
sol_nodes = np.empty(len(sol_node.path()))
for i, node in enumerate(sol_node.path()):
    sol_nodes[i] = node.state
path_cost = multi_g(graph, sol_nodes.astype(int))

s = ''
for i in range(len(path_cost)):
    if i < len(path_cost) - 1:
        s += '{} - [{}] -> '.format(int(sol_nodes[i]), int(path_cost[i+1] - path_cost[i]))
    else:
        s += '{}\n'.format(int(sol_nodes[i]))

s += 'Total Path Cost: {}'.format(int(path_cost[-1]))

print(s)
