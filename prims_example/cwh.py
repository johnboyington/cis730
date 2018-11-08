"""
Clarke-Wright Heuristic 
"""

import numpy as np

def tourlist(A):
    tour_set = []
    n = len(A)
    for i in range(n):
        T_i = [0, i, 0]
        tour_set.append(T_i)
    #print(tour_set)
    
    return tour_set

def CalcSavings(C):
    
    n = len(C)
    S = np.zeros((n,n))
    Savings_list = []
    for i in range(n):
        for j in range(n):
            S[i,j] = C[0,i] + C[j,0] - C[i,j]
            if i<j and S[i,j] != 0:
                Savings_list.append((i,j,S[i,j]))
    Savings_list = sorted(Savings_list, key = lambda x: x[2])
    for i,j,s in Savings_list: 
        s = '{:2} -> {:2} | {}'.format(i,j,s)
        #print(s)

    return S, Savings_list

def cwh(A, capacity, Q):
    S, Savings_list = CalcSavings(A)
    tour_set = tourlist(A)
    while Savings_list:
        i_s, j_s, s = Savings_list.pop()
        print(i_s, j_s, s)
        for t_i, tour in enumerate(tour_set):
            if i_s in tour:
                i_ti = t_i
                i_tour = tour
            if j_s in tour:
                j_ti = t_i
                j_tour = tour
        
        # calculate cost of summing both tours
        added_capacity = 0
        for t in i_tour:
            added_capacity += capacity[t]
        for t in j_tour:
            added_capacity += capacity[t]
        print(added_capacity)
        
        if i_tour[-2] == i_s and j_tour[1] == j_s:
            if i_ti != j_ti:
                if added_capacity <= Q:
                    new_tour = i_tour[:-1] + j_tour[1:]
                    tour_set.remove(i_tour)
                    tour_set.remove(j_tour)
                    tour_set.append(new_tour)
                    print(tour_set)
    return tour_set
    
    
    
            

A = np.loadtxt('cw_data.csv', delimiter=',')
cap = np.array([0, 10, 6, 6, 5, 7, 9, 6, 5, 5, 5, 3, 7])
Q = 30
tours = cwh(A, cap, Q)
print(tours)
