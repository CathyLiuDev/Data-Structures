def getName():
	return "Liu, Cathy"



class MyTree():
    def __init__(self, data):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = 0
        self.convertBinary = 0
        self.base = None
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data

    def insert(self, data):
        self.descendents += 1
        self.convertBinary = format(self.descendents+1, "b")
        self.convertBinary = self.convertBinary[1:]

        return self.insert1(self, data, self.convertBinary)
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted

    def insert1(self, root, data, treePath):
        if root is None:
            return MyTree(data)
        if treePath == "":
            root.left = self.insert1(root.left, data, treePath)
        elif treePath[0] == str(0):
            root.left = self.insert1(root.left, data, treePath[1:])
        else:
            root.right = self.insert1(root.right, data, treePath[1:])
        return root    
        
    def getHeight(self):
        # Return the height of this node
        return CheckHeight(self)


class MyBST(MyTree):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        self.descendents += 1
        #print("adding node: " + str(data))
        return self.insert1(self, data)
        
    def insert1(self, root, data):
        if root is None:
            return MyBST(data)
        if data < root.data:
            root.left = self.insert1(root.left, data)
        else:
            root.right = self.insert1(root.right, data)

        return root

    def CheckContains(self, tree, value):
        if tree is None:
            return False
        else:
            if (tree.data == value or self.data == value):
                return True

            result = self.CheckContains(tree.getLeft(), value)
            if not result:
                result = self.CheckContains(tree.getRight(), value)

        return result
    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        return self.CheckContains(self, data)

    def getHeight(self):
        # Return the height of this node
        return CheckHeight(self)

    def __assign__(self, value):
        return self.data


class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        self.base = self

    #def __repr__(self): 
    #    return repr(self.data)

    def __assign__(self, value):
        return self.data
    
    def getHeight(self, root):
        if root == None:           
            return -1
        else:
            return CheckHeight(root)

    def getBalanceFactor(self, root=None):
        # Return the balance factor of this node
        # height of left tree - height of right tree
        #  -2 = right heavy, +2 = left heavy
        if not root:
            return self.getHeight(self.left) - self.getHeight(self.right)
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        if not self.base and self.getHeight(self) == 0:
            self.base = MyAVL(self.data)
        else:
            self.base = self;

        self2 = self.insert1(self.base, data)    
        return self2

    def insert1(self, root, data):
        if root == None:
            newmy = MyAVL(data)
            return newmy
        elif data >= root.data:
            # add to right
            root.right = self.insert1(root.right, data)
            root.height += 1
            if root.getBalanceFactor(root) < -1:
                if root.right != None and root.left != None and root.right.getBalanceFactor(root.right) > 0:
                    root.right = self.singleRightRotate(root.right, True)
                if data >= root.data:
                    root = self.singleLeftRotate(root)
        elif data < root.data:
            root.left = self.insert1(root.left, data)
            root.height += 1
            if root.getBalanceFactor(root) > 1:
                if root.right != None and root.left != None and root.left.getBalanceFactor(root.left) < 0:
                    root.left = self.singleLeftRotate(root.left, True)
                if data < root.data:
                    root = self.singleRightRotate(root)
        return root


    def singleLeftRotate(self, root, condition = False):
        # Perform a left rotation on this node and return the new node in its spot
        if (root.right.right != None or condition):
            temp = root.right
            root.right = temp.left
            temp.left = root  
        else:
            temp = root.right.left
            temp.right = root.right
            temp.left = root
            root.right = None
            temp.right.left = None

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

    def singleRightRotate(self, root, condition = False):
        # Perform a right rotation on this node and return the new node in its spot
        if (root.left.left != None or condition):
            temp = root.left
            root.left = temp.right
            temp.right = root
        else:
            temp = root.left.right
            temp.left = root.left
            temp.right = root
            root.left = None
            temp.left.right = None
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

    def getLeft(self):
        # Return the left child of this node, or None
        if self.base == None:
            return self.left
        else:
            return self.base.left
    
    def getRight(self):
        # Return the right child of this node, or None
        if self.base == None:
            return self.right
        else:
            return self.base.right

def CheckHeight(tree):
    if tree is None:
        return -1
    else:
        return max(CheckHeight(tree.getLeft())+1,CheckHeight(tree.getRight())+1)
