import numpy as np
import sys
from ai_graph import AIGraph
from code import Graph_Problem, multi_g, h
from search import uniform_cost_search, greedy_best_first_graph_search, astar_search


# parse input and create problem
flag = sys.argv[1]
graph_name = sys.argv[2]
graph = AIGraph(graph_name)
graph.store_table()
graph.store_h()
problem = Graph_Problem(graph.S, graph.G, graph.filename)

# select search
if flag == '-bnb':
    sol_node = uniform_cost_search(problem)
elif flag == '-gbfs':
    sol_node = greedy_best_first_graph_search(problem, h)
elif flag == '-a':
    sol_node = astar_search(problem, h)
else:
    assert 'Not a valid flag.'

# grab data desired in printing
sol_nodes = np.empty(len(sol_node.path()))
for i, node in enumerate(sol_node.path()):
    sol_nodes[i] = node.state
path_cost = multi_g(graph, sol_nodes.astype(int))

# output solution data as string
s = ''
for i in range(len(path_cost)):
    if i < len(path_cost) - 1:
        s += '{} - [{}] -> '.format(int(sol_nodes[i]), int(path_cost[i+1] - path_cost[i]))
    else:
        s += '{}\n'.format(int(sol_nodes[i]))

s += 'Total Path Cost: {}'.format(int(path_cost[-1]))

print(s)
