import numpy as np


def initialize_tour(A):
    np.fill_diagonal(A, np.max(A))
    t0, t1 = np.unravel_index(np.argmin(A, axis=None), A.shape)
    nodes_remaining = list(range(len(A)))
    nodes_remaining.remove(t0)
    nodes_remaining.remove(t1)
    return [t0, t1, t0], nodes_remaining


def cost(A, T):
    """Returns the cost (float) given a tour (list)."""
    tour_cost = 0
    for i in range(len(T[:-1])):
        tour_cost += A[T[i], T[i+1]]


def next_minimum_distance(A, nodes_remaining, T):
    """Returns the closest neighbor to the tour."""
    connection = [T[0]] * len(T)
    costs = [float('inf')] * len(T)
    for node in nodes_remaining:
        for t in T:
            if A[node, t] < costs[nodes_remaining[node]]:
                costs[node] = A[node, t]
                connection[node] = t
    min_cost = min(costs)
    min_cost_index = costs.index(min_cost)
    return nodes_remaining[min_cost_index], connection[min_cost_index]


def insert_next_node(A, n, i, T):
    """Inserts the new neighbor into the tour."""
    # insert to left
    if A[T[i+1], n] > A[T[i-1], n]:
        T.insert(i, n)
    else:
        T.insert(i+1, n)
    return T


def nearest_insertion_heuristic(A):
    """Function that when given an adjacency matrix (np.array), returns a
    feasible tour (list) using the nearest insertion algorithm."""
    T, nodes_remaining = initialize_tour(A)
    while nodes_remaining:
        neighbor, i = next_minimum_distance(A, nodes_remaining, T)
        T = insert_next_node(A, neighbor, i, T)
        print(T)
        print(cost(A, T), '\n')
    return T


if __name__ == '__main__':
    A = np.loadtxt('tsp_data.csv', delimiter=',')
    A_tour = nearest_insertion_heuristic(A)
