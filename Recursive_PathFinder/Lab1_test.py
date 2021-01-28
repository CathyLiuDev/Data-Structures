# def findAllPaths(position, list):
#     x = V[position]
#     newPositionPositive = position + x
#     newPositionNegative = position - x
#     length = len(V)-1
#     print("integer at position " + str(position) + " is: " + str(x))
#     print("last index is: " + str(len(V) -1))
#     print("position + x is: " + str(newPositionPositive))
#     print("position - x is: " + str(newPositionNegative))
#     if 0 <= newPositionPositive <= length or 0 <= newPositionNegative <= length:
#         print("1")
#         return 1
#     else:
#         print("0")
#         return 0


# # 1.
# def findAllPaths(position, list):
#     # base case
#     x = V[position]
#     newPositionPositive = position + x
#     newPositionNegative = position - x
#     lastIndex = len(list) -1
#     if position == lastIndex:
#         print("one valid path found, ending position: " + str(position))
#         return 1
#     # recursive case
#     else:
#         if 0 <= newPositionPositive <= lastIndex:
#             print("using newPositionPositive: " + str(newPositionPositive))
#             return findAllPaths(newPositionPositive, list)
#         elif 0 <= newPositionNegative <= lastIndex:
#             print("using newPositionNegative: " + str(newPositionNegative))
#             return findAllPaths(newPositionNegative, list)
#         else:
#             print("no valid paths found")
#             return 0

# # 2. adding Solutions param
# def findAllPaths(position, list, solutions):
#     # base case
#     # solutions is an empty list to be passed in?
#     x = list[position]
#     newPositionPositive = position + x
#     newPositionNegative = position - x
#     lastIndex = len(list) -1
#     if position == lastIndex:
#         print("one valid path found, ending position: " + str(position))
#         # add solutions list to paths list, append not extend
#         # if solutions in paths:
#         #     return findAllPaths(position, )
#         # else:
#         #     paths.append(solutions)
#         # print(paths)
#         paths.append(solutions)
#         print(paths)        
#         return 1
#     # recursive case
#     else:
#         if 0 <= newPositionPositive <= lastIndex:
#             print("using newPositionPositive: " + str(newPositionPositive))
#             solutions.append(list[position])
#             print(solutions)
#             return findAllPaths(newPositionPositive, list, solutions)
#         elif 0 <= newPositionNegative <= lastIndex:
#             print("using newPositionNegative: " + str(newPositionNegative))
#             solutions.append(list[position])
#             print(solutions)
#             return findAllPaths(newPositionNegative, list,solutions)
#         else:
#             print("no valid paths found")
#             return 0


# I = [0,1,2,3,4,5,6]
# # V = [1,4,3,5,4,7,3]
# V = [1,5,3,5,4,7,3]

# # trying to save position instead of value
# paths = []
# # solutions = []

# findAllPaths(4,V, solutions = [])
class Pathfinder():
    def __init__(self, vector):
        # Initialize the Pathfinder object
        self.vector = vector
        self.paths = []
        self.findAllPaths(0,[])

    def findAllPaths(self, position, solution=[], nodes = []):
        # base case
        # solutions is an empty list to be passed in?
    
        lastIndex = len(self.vector) -1
        if position == lastIndex:
            print("one valid path found, ending position: " + str(position))
            # add solutions list to paths list, append not extend
            # if solutions in paths:
            #     return findAllPaths(position, )
            # else:
            #     paths.append(solutions)
            # print(paths)
            self.paths.append(solution)
            print(self.paths)        
        # recursive case
       

        # elif position < 0 and position + self.vector[position] >= lastIndex:
            # x = self.vector[position]
            # if position + x <= lastIndex:
                # newPositionPositive = position + x
            # self.findAllPaths(position + self.vector[position], solution)
        # elif position >= lastIndex and position - self.vector[position] > 0:
            # x = self.vector[position]
            # if position - x > 0:
                # newPositionNegative = position - x
            # self.findAllPaths(position - self.vector[position], solution)
            # print(solution) 
            # return solution.append(position)

        elif position in solution:
            x = self.vector[position]
            newPositionPositive = position + x
            newPositionNegative = position - x
            self.findAllPaths(newPositionPositive, solution)
            self.findAllPaths(newPositionNegative, solution)
            # print(solution) 
            # return solution.append(position)

        else:
            if 0 <= position <= lastIndex:
                if position < 0:
                    print(solution)
                    self.findAllPaths(position + self.vector[position], solution)
                elif position >= lastIndex:
                    print(solution)
                    self.findAllPaths(position - self.vector[position], solution)
                else:
                    solution.append(position)
    def getPaths(self):
        # Return the list of viable paths, or [None] if there are no solutions
        return self.paths
I = [0,1,2,3,4,5,6]
# V = [1,4,3,5,4,7,3]
# V = [1,2,3,5,4,7,3]s
V = [4,4,1,2,3,1,8,2,0]

finder = Pathfinder(V)
finder.findAllPaths
finder.getPaths


# trying to save position instead of value
# paths = []
# findAllPaths(0,V, solutions = [])