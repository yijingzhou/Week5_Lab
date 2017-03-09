# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:54:44 2017

@author: Mebius
"""

def powerset_recursion_comp(l):
    # Base case: the empty set
    if not l:
        return [[]]
    # The recursive relation
    # Do a powerset call for l[1:]
    # Add lists of all combinations of the 1st element (l[0]) with other elements' powersets
    return powerset_recursion_comp(l[1:]) + [[l[0]] + x for x in powerset_recursion_comp(l[1:])]

def powerset_recursion(l):
    if not l:
        return [[]]
    subset = []
    for x in powerset_recursion(l[1:]):
        subset.append([l[0]] + x)    
    return powerset_recursion(l[1:]) + subset
    
def main():

    num_items = 4
    my_list = list(range(num_items))
    print(my_list)
    
    my_pset = powerset_recursion(my_list)
    print("using recursion:\n", my_pset)

    my_pset = powerset_recursion_comp(my_list)
    print("using recursion:\n", my_pset)    
main()