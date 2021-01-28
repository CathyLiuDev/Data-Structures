import heapq
import operator

def getName():
	return "Liu, Cathy"

def gen_huffman_code(node, codeMap, buffer=[]):
    if not node.Left and not node.Right:
        codeMap[node.Char] = ''.join(buffer)
        return
    buffer.append('0')
    gen_huffman_code(node.Left, codeMap, buffer)
    buffer.pop()

    buffer.append('1')
    gen_huffman_code(node.Right, codeMap, buffer)
    buffer.pop()

class MyHuffman():
    
    def __init__(self):
        # Initialize this stack, and store data if it exists
        self.Root = None
        self.CodeMap={}
    
    def build(self, weights):
        # Build a huffman tree from the dictionary     
        nodes = []
        for weight in weights:
            nodes.append(Node(weight, weights[weight]))
   
        nodes.sort(key=operator.attrgetter('Freq'))
        while(True):
            if len(nodes)>1:
                first=nodes.pop(0)
                second=nodes.pop(0)
            else:
                first=nodes[0]
                second=None
      
            if not second:
                self.Root = first;
                return first
            parent = Node(None, first.Freq + second.Freq, first, second)
            nodes.insert(0, parent)
            nodes.sort(key=operator.attrgetter('Freq'))

    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        if self.Root:
            gen_huffman_code(self.Root, self.CodeMap)

        bitString = ''
        for c in word:
            if c in self.CodeMap.keys():
                bitString += ''.join(self.CodeMap[c])
        
        return bitString
 
    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        string = ""
        bitTemp = ""
        for i in range(0, len(bitstring)):
            bitTemp += ''.join(bitstring[i])
            for key, bits in self.CodeMap.items():
                if bits == bitTemp:
                    string += ''.join(key)
                    bitTemp = ""

        return string
        

# This node structure might be useful to you
class Node:
    def __init__(self, value, data, left=None, right=None):
        self.Char = value
        self.Freq = data
        self.Left = left
        self.Right = right
