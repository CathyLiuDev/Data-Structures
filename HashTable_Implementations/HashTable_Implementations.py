# You may not use dicts.
def getName():
	return "Liu, Cathy"
	
class MyHashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        self.map = [None]*size
        self.hash1 = hash1
        self.length = 0

    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        hashedKey = self.hash1(key)
        if key == "":
            return False
        if self.map[hashedKey] == None:
            self.length += 1
            self.map[hashedKey] = data
            return True
        else:
            return False
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        hashedKey = self.hash1(key)
        if self.map[hashedKey] == "":
            return None
        if self.map[hashedKey] != None:
            temp = self.map[hashedKey]
            self.map[hashedKey] = None
            return temp
        return None
        
    def __len__(self):
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        if self.length < len(self)-1:
            return False
        else:
            return True

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        pass
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        hashedKey = self.hash1(key)
        if key == "":
            return False
        if self.map[hashedKey] == None:
            self.length += 1
            self.map[hashedKey] = [data]
            return True
        else:
            self.length += 1
            self.map[hashedKey].append(data)
            return True

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        hashedKey = self.hash1(key)
        if key == "":
            return None
        if self.map[hashedKey] != None:
            temp = self.map[hashedKey][0]
            if len(self.map[hashedKey]) > 1:
                self.map[hashedKey] = self.map[hashedKey][1:]
            else:
                self.map[hashedKey] = None
            return temp
        return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.size = size
        self.hash2 = hash2
        pass
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        hashedKey = self.hash1(key)
        probeDistance = self.hash2(hashedKey)
        keyValPair = [key, data]
        path = []
        if key == "":
            return False
        if self.map[hashedKey] == None:
            self.length += 1
            self.map[hashedKey] = keyValPair
            return True
        else:
            position = hashedKey
            while True:
                position = position - probeDistance
                if self.map.count(None) == 0:
                    #print("list has one spot left")
                    return False
                if position < 0:
                    position = self.size - abs(position)
                if self.map[position] == None:
                    self.map[position] = keyValPair
                    self.length += 1 
                    return True
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        hashedKey = self.hash1(key)
        probeDistance = self.hash2(hashedKey)
        if key == "":
            return None
        if self.map[hashedKey] != None and self.map[hashedKey][0] == key:
            return self.map[hashedKey][1]
        if self.map[hashedKey] != None and self.map[hashedKey][0] != key:
            position = hashedKey
            while True:
                position = position - probeDistance
                if position < 0:
                    position = self.size - abs(position)
                if self.map[position][0] == key:
                    return self.map[position][1]
        return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.length

