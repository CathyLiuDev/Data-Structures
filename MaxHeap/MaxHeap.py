import math

def getName():
	return "Liu, Cathy"

class MyHeap():
    def __init__(self, array):
        # Create a heap from the passed array. The first element should be None.
        self.impleList = sorted(array, reverse = True)
        self.newList = [-2]*100
        self.newList[0] = -1
        for i in range (0, len(self.impleList)):
            self.newList[i+1] = self.impleList[i]
        self.size = len(self.impleList)
        self.lastIndex = self.size
        #print(self.size)



    def insert(self, data):
        # Insert an item in to the heap.
        # This method should be able to handle items above and beyond the initial capacity
        self.size += 1
        self.lastIndex +=1
        tempIndex = self.lastIndex       
        if data in self.newList:
            self.lastIndex -= 1
            return
        else:
            self.newList[self.lastIndex] = data
            self.reheapifyUp(tempIndex)
 
    def reheapifyUp(self, index):

        while self.newList[index] > self.newList[self.getParentIndex(index)] and index > 0:
            if self.newList[self.getParentIndex(index)] == -1:
                break
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)
            # self.reheapifyUp(index)


    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False

    def reheapifyDown(self, index):
        if not self.isLeaf(index): 
            if (self.newList[index] < self.newList[self.getLeftIndex(index)] or
                self.newList[index] < self.newList[self.getRightIndex(index)]): 
                if self.newList[self.getLeftIndex(index)] > self.newList[self.getRightIndex(index)]: 
                    self.swap(index, self.getLeftIndex(index)) 
                    self.reheapifyDown(self.getLeftIndex(index)) 
                else: 
                    self.swap(index, self.getRightIndex(index)) 
                    self.reheapifyDown(self.getRightIndex(index)) 

    def swap(self, i, j): 
        self.newList[i], self.newList[j] = self.newList[j], self.newList[i] 

    def extractMax(self):
        # Return the largest item in the heap, but ensure that the heap property is maintained
        maxVal = self.newList[1]
        self.newList[1] = self.newList[self.lastIndex]
        self.size -= 1
        self.reheapifyDown(1)
        return maxVal

    def __len__(self):
        # Return the number of items currently in the heap
        return self.size

    def getData(self):
        # Return the current heap as an array that does not use the first value
        data = []
        for i in range(0, len(self.newList)-1):
            if self.newList[i] != -2:
                data.append(self.newList[i])
        #print(data)
        return data

    def getParentIndex(self, index):
        return index // 2

    def getRightIndex(self, index):
        return 2*index + 1

    def getLeftIndex(self, index):
        return 2*index

    #def printHeap(self): 
    #    for i in range(1, (self.size//2)+1): 
    #        print(" PARENT : "+str(self.newList[i])+" LEFT CHILD : "+ 
    #                           str(self.newList[2 * i])+" RIGHT CHILD : "+
    #                           str(self.newList[2 * i + 1])) 

