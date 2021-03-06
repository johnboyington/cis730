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
    return tour_cost


def next_minimum_distance(A, nodes_remaining, T):
    """Returns the closest neighbor to the tour."""
    connection = [T[0]] * len(nodes_remaining)
    costs = [float('inf')] * len(nodes_remaining)
    for n_i, node in enumerate(nodes_remaining):
        for t_i, t in enumerate(T):
            if A[node, t] < costs[n_i]:
                costs[n_i] = A[node, t]
                connection[n_i] = t
    min_cost = min(costs)
    min_cost_index = costs.index(min_cost)
    T_i = T.index(connection[min_cost_index])
    node = nodes_remaining.pop(min_cost_index)
    return node, T_i


def insert_next_node(A, n, i, T):
    """Inserts the new neighbor into the tour."""
    print(n+1)
    min_cost = np.max(A) * 2
    for t_i in range(len(T[1:])):
        c_next = A[n, T[t_i + 1]] + A[T[t_i], n] - A[T[t_i + 1], T[t_i]]
        if c_next < min_cost:
            min_cost = c_next
            min_cost_i = t_i + 1
    T.insert(min_cost_i, n)
    return T


def nearest_insertion_heuristic(A):
    """Function that when given an adjacency matrix (np.array), returns a
    feasible tour (list) using the nearest insertion algorithm."""
    T, nodes_remaining = initialize_tour(A)
    print('', list(np.array(T) + 1))
    print('Total Path Cost:  ', cost(A, T), '\n')
    while nodes_remaining:
        neighbor, i = next_minimum_distance(A, nodes_remaining, T)
        T = insert_next_node(A, neighbor, i, T)
        print('', list(np.array(T) + 1))
        print('Total Path Cost:  ', cost(A, T), '\n')
    return T


if __name__ == '__main__':
    A = np.loadtxt('tsp_data.csv', delimiter=',')
    A_tour = nearest_insertion_heuristic(A)
