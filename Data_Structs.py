"""
Python Data Struct Refresher 
"""
import util
import heapq
'''
Stacks Are LiFo 
push -> append
pop -> delete back
'''
def stackFill(arr):
    print("Filling Stack...")
    for i in range(0,10):
        arr.push(i)
    return arr

def stackCheck(arr):
    print("Init Arr: " + str(arr))
    arr.pop()
    print("Removed item: " + str(arr))
    arr.pop()
    print("Removed item: "  + str(arr))
    print("Res Arr: " + str(arr))

'''
Queues are FiFo
push -> enqueue = add to front
pop -> dequeue = delete from back
'''
def queueFill(arr):
    print("Filling Queue...")
    for i in range(10):
        arr.push(i)
    return arr

def queueCheck(arr):
    print("Init Arr: " + str(arr))
    arr.pop()
    print("Dequeue: " + str(arr))
    arr.pop()
    print("Dequeue: " + str(arr))
    print("Res Arr: " + str(arr)) 

def priorityQueueFill(arr):
    print("Filling Priority Queue...")
    val = ['Cat','Dog','Goat','Frog', 'Hyena','Lion','Tiger','Snake','Hippo','Moose']
    for i in range(5):
        heapq.heappush(arr,((i,val[i])))
    heapq.heapify(arr)
    return arr

def priorityQueueCheck(arr):
    print("Init Arr: " + str(arr))
    heapq.heappop(arr)
    print("Removing item: " + str(arr))
    heapq.heappop(arr)
    print("Removing item: " + str(arr))
    print("Res Arr: " + str(arr))

def printPQ(arr):
    pq = list(arr)
    for x in pq:
        print(x, end=' ') 


def main():
    s = util.Stack()
    sFill = stackFill(s)
    sChk = stackCheck(sFill)

    q = util.Queue()
    qFill = queueFill(q)
    qChk = queueCheck(qFill)

    pq = []
    pqFill = priorityQueueFill(pq)
    pqChk = priorityQueueCheck(pqFill)

if __name__ == "__main__":
    main()