import numpy as np
import pickle
from search import Problem


# ______________________________________________________________________________
def h(n):
    '''The hueristic function'''
    h_array = np.load('h.npy')
    return h_array[n.state]


# ______________________________________________________________________________
class Graph_Problem(Problem):
    '''Like the abstract Problem class, but allows me to lookup actions using
    the pickled cost matrices.'''
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
    '''Given a series of nodes, prints the cumulative cost to arrive at each node.'''
    sol = np.zeros(len(nodes))
    for i, node in enumerate(nodes):
        if i == 0:
            sol[i] = 0
        else:
            sol[i] = sol[i-1] + graph.cost[nodes[i-1], node]
    return sol
