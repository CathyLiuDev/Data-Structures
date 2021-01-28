import random
import string
import re
import math
#Module Imports
import sys
from importlib import import_module

def GenerateArray(size=10):
    if (size <= 1) :
        size = 2
    elif (size > 50):
        size = 50
    data = []
    for i in range(1,size):
        data.append(random.randint(0, size))
    data.append(0)

    return data

def CheckHeapness(heap):
    if len(heap) < 2:
        return True # 1 element heap is trivially correct
    data = heap.getData()
    for i in range(len(data)-1, 1, -1):
        #print(f"Checking {i}")
        if data[i] > data[math.floor(i/2)]:
            return False
    return True

def Test(lib, seed=0, size=10, rounds=10, verbose=False ):
    if not lib:
        print("You need to include a testable library")
        return False
    random.seed(a=seed)




    data = [1,2,3,4,5]

    flag = True

    try:
        heap = lib.MyHeap(data.copy())
    except:
        if verbose:
            print("Error: Heap not creatable.")
        flag = False

    if not CheckHeapness(heap):
        if verbose:
            print("Error: Initial heap creation does not maintain heap property.")
        flag = False

    count = 0
    for elem in data:
        try:
            heap.insert(elem)
        except:
            if verbose:
                print("Error: Heap element not insertable.")
            flag = False
            break
        if not CheckHeapness(heap):
            if verbose:
                print("Error: Individual insertion does not maintain heap property.")
            flag = False
            break
        count += 1
        if len(heap) != len(data) + count:
            if verbose:
                print("Error: Heap item count incorrect after indiviual insertion.")
            flag = False
            break


    data = data + data

    if verbose:
        if flag:
            print("Heap individual insertion test complete")
        else:
            print("Heap individual insertion test failed")
    yield flag

    try:
        val=heap.extractMax()
    except:
        if verbose:
            print("Error: Element not extracted")
        return False

    if val != 5:
        if verbose:
            print("Error: Heap extraction returning incorrect element")
        return False
    if len(heap) != len(data)-1:
        if verbose:
            print("Error: Heap size incorrect after extraction")
        return False

    if verbose:
        print("Heap extraction test complete")
    yield True
    

    data = [1]
    try:
        heap = lib.MyHeap(data)
    except:
        if verbose:
            print("Error: Heap not recreatable.")
        return False
     
    newdata = GenerateArray(size)
    for elem in newdata:                
        try:
            heap.insert(elem)
        except:
            if verbose:
                print("Error: Heap element not insertable.")
            return False
        if not CheckHeapness(heap):
            if verbose:
                print("Error: Individual insertion does not maintain heap property.")
            return False

    data = data + newdata
    if len(heap) != len(data):
        if verbose:
            print("Error: Heap item count incorrect after batch insert.")
        return False

    if verbose:
        print("Batch individual insertion test complete")
    yield True

    flag = True
    try:
        m = heap.extractMax()
        if not CheckHeapness(heap):
            if verbose:
                print("Error: Extraction does not maintain heap property.")
            flag = False
        heap.insert(m+1)
        if (m+1) != heap.extractMax():
            if verbose:
                print("Error: Insertion does not maintain heap property.")
            flag = False
    except:
        if verbose:
            print("Error: Heap element not insertable.")
        flag = False

    if verbose:
        if flag:
            print("Heap reinsertion test complete")
        else:
            print("Heap reinsertion test failed")
    
    yield flag

    data = sorted(data, reverse=True)    
    data.pop()
    count = len(data)

    
    flag = True
    heapsorted = []
    for i in range(count):
        
        try:
            heapsorted.append(heap.extractMax())
        except:
            if verbose:
                print("Error: Element not extracted.")
            flag = False
            break
        
        if not CheckHeapness(heap):
            if verbose:
                print("Error: Extraction does not maintain heap property.")
            flag = False
            break

    for i in range(len(heapsorted)-1):
        if heapsorted[i]<heapsorted[i+1]:
            if verbose:
                print("Error: Extraction does not return sorted list")
            flag = False
            break

    if verbose:
        if flag:
            print("Heapsort test complete")
        else:
            print("Heapsort test failed")
    yield flag



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Include at least a library name as an argument.")
        exit()
    name = sys.argv[1]
    if name.startswith(".\\"):
        name = name[2:]
    if name.endswith(".py"):
        name = name[:-3]
    module=import_module(name,package=__name__)
    print(f"Testing module {name} by {module.getName()}")
    score = 0
    for i in Test(module,seed=654654, size=1000, rounds=200, verbose=True):
        if i:
            score+=1
        

    print(f"Test result: {score}/5")