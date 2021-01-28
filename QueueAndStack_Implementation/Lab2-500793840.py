def getName():
	return "Liu, Cathy"
	
class MyQueue:
    def __init__(self, data=-1):
        # Initialize this queue, and store data if it exists
        if data == -1:
            self.queue = None
            self.length = 0
        else:
            self.queue = Node(data)
            self.length = 1


    def enqueue(self, data):
        # Add data to the end of the queue
        if self.queue == None:
            self.queue = Node(data)
        else:
            checked = self.queue
            targetNode = None
            while checked != None:
                targetNode = checked
                checked = checked.linked
                if checked == None:
                    break
            targetNode.linked = Node(data)
        self.length += 1

    def dequeue(self):
        # Return the data in the element at the beginning of the queue, or None if the queue is empty
        if self.length > 0:
            self.length -= 1
        temp = self.queue
        self.queue = self.queue.linked
        return temp.data

    def __len__(self):
        # Return the number of elements in the stack
        return self.length

class MyStack:
    def __init__(self, data=-1):
        # Initialize this stack, and store data if it exists
        if data == -1:
            self.stack = None
            self.length = 0
        else:
            self.stack = Node(data)
            self.length = 1
    
    def push(self, data):
        # Add data to the beginning of the stack
        if self.stack == None:
            self.stack = Node(data)
        else:
            temp = Node(data)
            tempS = self.stack
            temp.linked = tempS
            self.stack = temp
        self.length += 1

    def pop(self):
        # Return the data in the element at the beginning of the stack, or None if the stack is empty
        if self.length > 0:
            self.length -= 1

        temp = self.stack
        self.stack = self.stack.linked
        return temp.data


    def __len__(self):
        # Return the number of elements in the stack
        return self.length


class Node:
    def __init__(self, data, linked=None):
        # Initialize this node, insert data, and set the next node if any
        self.data = data
        self.linked = linked
    def __str__(self):
        return str(self.data)
