#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Martin Urueta - 10/22/2022
#


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE
        self.start_location = problem.start
        self.goal_location = problem.goal
        self.speed = 0.0

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            for locs in self.problem.map.loc_dict: # this is to figure out the action cost; action cost -> current node and children node; actioncost = t 
                for connection in self.problem.map.connection_dict:
                    tmpRoadCost = self.problem.map.get(locs,connection)
                    if tmpRoadCost is not None:
                        tmpdis = self.problem.map.euclidean_distance(locs,connection)
                        tmpSpeed = tmpdis / tmpRoadCost
                        if tmpSpeed > self.speed: # find the max time
                            self.speed = tmpSpeed
                
            value = self.problem.map.euclidean_distance(loc, self.goal_location) # figure out euclidean_distance aka Pythagorean theroem
            value = value / self.speed # distance / time = speed
            return value

