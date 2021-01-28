def getName():
	return "Liu, Cathy"

class charNode:
    def __init__(self, char):
        self.char = char
        self.frequency = 0
        self.isEnd = False
        self.leafNode = None
    def __repr__(self):
        return self.char

class MyTrie:
    def __init__(self, level=None):
        self.level = level
        self.nextLevel = None
        self.letters = [None]*54
        self.length = 0
        self.suggestions = []

    def __repr__(self):
        return str(self.level)
  
    def checkMatch(self, char, node):
        if node == None:
            return False
        elif char == node.char:
            return True
        else:
            return False
    
    def convert(self, string): 
        str = "" 
        return(str.join(string)) 


    def insert(self, word):
        chars = list(word)
        self.length += 1
        if self.nextLevel == None:
            self.nextLevel = MyTrie(1)
        self.insert1(self, chars, 0)
        return self

    def insert1(self, root, word, counter):
        if counter <= len(word):
            if counter < len(word):
                currentChar = word[counter]
                charIndex = self.getCharIndex(currentChar)
                if root.letters[charIndex] == None:
                    root.letters[charIndex] = charNode(currentChar)
                    root.letters[charIndex].frequency += 1
                    if counter == len(word) - 1:
                        stringWord = self.convert(word)
                        if root.letters[charIndex].leafNode == None:
                            root.letters[charIndex].leafNode = leafNode(stringWord)
                        else:
                            root.letters[charIndex].leafNode.word.append(stringWord)
                    root = root.nextLevel
                    if root.nextLevel == None:
                        root.nextLevel = MyTrie(counter+2)
                    return self.insert1(root, word, counter+1)
                else:
                    root.letters[charIndex].frequency += 1
                    if counter == len(word) - 1:
                        stringWord = self.convert(word)
                        if root.letters[charIndex].leafNode == None:
                            root.letters[charIndex].leafNode = leafNode(stringWord)
                        else:
                            root.letters[charIndex].leafNode.word.append(stringWord)
                    root = root.nextLevel
                    if root.nextLevel == None:
                        root.nextLevel = MyTrie(counter+2)
                    return self.insert1(root, word, counter+1)
        else:
            print("word already inserted")
            return root


    def exists(self, word, position=0):
        temp = self.getAllWordsforNode(self, [], word)
        if word in temp:
            return True
        else:
            return False

    def autoComplete(self, prefix, counter = 0):
        self.suggestions = []
        temp = self.autoComplete1(self, prefix, counter)
        if self.suggestions != None and len(self.suggestions) >0:
            return self.suggestions
        else:
            return temp
    def autoComplete1(self, root, prefix, counter):
        if prefix == "":
            return self.getAllWordsforNode(root, [], prefix)
        else:
            currentChar = prefix[counter]
        found = False
        if counter == len(prefix) - 1 or prefix == "":
            for charNode in root.letters:
                if charNode != None and self.checkMatch(currentChar, charNode):
                    found = True
                    currentNode = charNode
                    temp = self.getAllWordsforNode(root, [], prefix)
                    return temp

      
        if counter < len(prefix):
            for charNode in root.letters:
                if charNode != None and self.checkMatch(currentChar, charNode):
                    found = True
                    currentNode = charNode
                    temp = self.autoComplete1(root.nextLevel, prefix, counter+1)
                    if temp == []:
                        return []
        if not found:
            return []
        else:
            return self.suggestions

    def getAllWordsforNode(self, root, solution, prefix):
        if root == None:
            return solution
        for charNode in root.letters:
            if charNode != None:
                if charNode.leafNode != None and charNode.leafNode.word != None:
                    for e in charNode.leafNode.word:
                        if e.startswith(prefix) or prefix == e and e not in solution:
                            solution.append(e)
        self.getAllWordsforNode(root.nextLevel, solution, prefix)
        newList = sorted(solution)
        if newList != None and len(newList)>0:
            self.suggestions = newList
        return newList
        
            
    def getCharIndex(self, char):
        if ord('A') <= ord(char) <= ord('Z'):
            charIndex = ord(char) - ord('A')
        elif ord('a') <= ord(char) <= ord('z') :
            charIndex = ord(char) - 71
        else:
            charIndex = 52
        return charIndex


    def __len__(self):
        return self.length

class leafNode:
    def __init__(self, word):
        self.word = [word]           
    def __repr__(self):
        return self.word
