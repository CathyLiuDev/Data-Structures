def getName(): 
	return "Liu, Cathy"
	

class Pathfinder():
    def __init__(self, vector):
        self.vector = vector
        self.paths = []

    def findAllPaths(self, position=0, solution=[]):
        # initialize with position at index 0 and solution is an empty list
        # base case - if invalid, return    
        #  invalid if out of bounds or already have the index on the path
        lastIndex = len(self.vector)-1
        if  position > lastIndex or position < 0 or position in solution:
            # prevent underflow
            if len(solution) > 0:
                solution.pop()
            return
        solution.append(position)
        # base case - if reached last index - add solution to paths list and continue exploring
        # from last valid index
        if position == lastIndex:
            self.paths.append(solution.copy())
            # prevent underflow
            if len(solution) > 0:
                solution.pop()
        # recursive case - explore both index +/- value at index
        else:
            x = self.vector[position]
            self.findAllPaths(position + x, solution)
            self.findAllPaths(position - x, solution)
            
    def getPaths(self):
        # if no valid paths recorded, return [None]
        if self.paths == []:
            # print("None")
            return [None]
        # if valid paths found, print as list of lists
        else:
            # print(self.paths)
            return self.paths