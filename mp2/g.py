import numpy as np


def g(graph, nodes):
    sol = np.zeros(len(nodes))
    for i, node in enumerate(nodes):
        if i == 0:
            sol[i] = 0
        else:
            sol[i] = sol[i-1] + graph.cost[i-1, node]
    return sol
