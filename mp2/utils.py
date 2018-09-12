import numpy as np


class Node(object):
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

def child_node(problem, parent, action):
    

def multi_g(graph, nodes):
    sol = np.zeros(len(nodes))
    for i, node in enumerate(nodes):
        if i == 0:
            sol[i] = 0
        else:
            sol[i] = sol[i-1] + graph.cost[i-1, node]
    return sol


def g(graph, nodes):
    for i, node in enumerate(nodes):
        if i == 0:
            sol[i] = 0
        else:
            sol[i] = sol[i-1] + graph.cost[i-1, node]
    return sol


def my_insert(frontier, child):
    child_index = 0
    for i, node in enumerate(frontier):
        if node[0] == child[0]:
            if child[1] < node[1]:
                frontier[i] = child
                return frontier
            else:
                return frontier
        if node[1] > child[1]:
            child_index = i
    return frontier.insert(child_index, child)


def branch_and_bound(problem):
    '''
    Returns a solution or failure.
    '''
    node = problem.S, 0
    frontier = [node]
    explored = []
    while True:
        if len(frontier) == 0:
            return 'Failure'
        node = frontier.pop()
        if problem.G == node[0]:
            return node
        explored.append(node[0])
        for i, action in enumerate(problem.cost[node[0]]):
            if action != -1:
                child = i, g(problem, i)
                if child not in explored or child not in frontier:
                    frontier = my_insert(frontier, child)
