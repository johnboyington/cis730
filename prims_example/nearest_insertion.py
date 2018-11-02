import numpy as np


def cost(T):
    """Returns the cost (float) given a tour (list)."""
    pass


def next_minimum_distance(remaining, T):
    """Returns the closest neighbor to the tour."""
    pass


def insert_next_node(n, i, T):
    """Inserts the new neighbor into the tour."""
    pass


def nearest_insertion_heuristic(A):
    """Function that when given an adjacency matrix (np.array), returns a
    feasible tour (list) using the nearest insertion algorithm."""
    nodes_remaining = list(range(len(A)))
    T = []
    while nodes_remaining:
        neighbor, i = next_minimum_distance(nodes_remaining, T)
        T = insert_next_node(neighbor, i, T)
        print(T)
        print(cost(T), '\n')
    return T