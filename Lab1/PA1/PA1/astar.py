#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Martin Urueta - 10/22/2022
#


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    Locate = Node(problem.start, h_eval= h.h_cost(problem.start)) # node <- a node containing the initial state of problem
    if problem.is_goal(Locate.loc): # if node contains a goal state of problem then return node
        return Locate
    Frontier_queue = Frontier(Locate, sort_by ='f') # initialize the frontier to contain node # For the frontier, use a priority queue that sorts by f(n) cost.
    reach_set = set() # initialize the reached set to contain node
    reach_set.add(Locate)
    while not Frontier_queue.is_empty(): # while frontier is not empty
        tempQueue = Frontier_queue.pop() # node <- a leaf node removed from frontier
        if problem.is_goal(tempQueue.loc): # if node contains a goal state of problem then return node
            return tempQueue
        templist = tempQueue.expand(problem, h_fun = h) # expand node
        for node in templist: # for each child of node
            if (repeat_check == True): #checking if true, and find node in list, should not add it to frontier
                if (node in reach_set): # if child is in the reached set
                    if ((node in Frontier_queue )and (Frontier_queue[node] > node.value("f"))): # if child is in frontier but with a higher cost
                        Frontier_queue.__delitem__(node) # remove the matching node from frontier
                        Frontier_queue.add(node) # add child to frontier
                else:
                    Frontier_queue.add(node) # add child to frontier
                    reach_set.add(node) # add child to the reached set
            else:
                Frontier_queue.add(node) # add child to frontier
                reach_set.add(node) # add child to the reached set

    return None # return failure
