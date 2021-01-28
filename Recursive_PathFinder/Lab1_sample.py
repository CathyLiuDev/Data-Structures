
class Pathfinder():
    def __init__(self, vector):
        self.vector = vector
        self.paths = []

    def findAllPaths(self, position=0, solution=[]):
        # base case - if invalid, return    
        #  invalid if: out of bounds or already have the index on the path
        lastIndex = len(self.vector)-1
        if  position > lastIndex or position < 0 or position in solution:
            if len(solution) > 0:
                solution.pop()
            return
        solution.append(position)
        # base case - if reached last index - add solution to paths list and continue exploring
        # from last valid index
        if position == lastIndex:
            self.paths.append(solution.copy())
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

I = [0,1,2,3,4,5,6,7,8,9,10,11]
# V = [1,4,3,5,4,7,3]
# V = [4,3,1,2,3,5,4,2,2,1,1,0]
# V = [2,3,1,1,0]
# V = [4,4,1,2,3,1,8,2,0]
# V = [3, 1, 1, 1, 3, 4, 2, 5, 3, 0]
V = [2, 8, 3, 2, 7, 2, 2, 3, 2, 1, 3, 0]
finder = Pathfinder(V)
finder.findAllPaths()
finder.getPaths()

# The Pathfinder class is initialized with a list of integers, the target of which is the position with value 0.
# The findAllPaths method recursively explores the list.
# The getPaths method returns the list of viable paths, or [None] if there are no solutions
#updated the method signature to use default value of 0 for position and empty list for solution
#so that the method can simply be invoked by findAllPaths() without any arguments
