import numpy as np
import pickle
from search import Problem, Node, uniform_cost_search


# ______________________________________________________________________________
def child_node(problem, parent, action):
    pass



# ______________________________________________________________________________
class Graph_Problem(Problem):
    def __init__(self, initial, goal, lookup_name):
        Problem.__init__(self, initial, goal)
        self.lookup = pickle.load(open(lookup_name[:-4] + '.p', 'rb'))

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        return list(range(len(self.lookup[state])))

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return self.lookup[state][action][0]

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action."""
        return c + self.lookup[state1][action][1]


# ______________________________________________________________________________
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
