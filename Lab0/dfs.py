#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
# Me and Angelo have disscuss this through whiteboard
# I used Generic Search pseudo code and as well as Uniform-Cost Search to implement repeated checks
# https://www.w3schools.com/python/python_sets.asp I used python set to be able to store in a set as stated in the generic search
# I used the same code as bfs since Generic search and uniform-Cost search works for both Queue and stack 
# this Stack problem (Last in; First Out) First |5|4|3|2|1| Last
# Martin Urueta - 10/4/2022
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    Locate = Node(problem.start) # node <- a node containing the initial state of problem
    if problem.is_goal(Locate.loc): # if node contains a goal state of problem then return node
        return Locate
    Frontier_Stack = Frontier(Locate,queue=False) # initialize the frontier to contain node
    reach_set = set() # initialize the reached set to contain node
    reach_set.add(Locate)
    while not Frontier_Stack.is_empty(): # while frontier is not empty
        tempStack = Frontier_Stack.pop() # node <- a leaf node removed from frontier
        if problem.is_goal(tempStack.loc): # if node contains a goal state of problem then return node
            return tempStack
        templist = tempStack.expand(problem) # expand node
        for node in templist: # for each child of node
            if (repeat_check == True): #checking if true, and find node in list, should not add it to frontier
                if (node not in reach_set): # if child is in the reached set
                    Frontier_Stack.add(node) #add child to frontier stack
                    reach_set.add(node) #add child to reach set
            else:
                Frontier_Stack.add(node) #add child to frontier stack
                if (node not in reach_set): # if child is in the reached set
                    reach_set.add(node) #add child to reach set 
    return None # return failure
