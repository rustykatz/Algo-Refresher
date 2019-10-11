"""
Python Data Struct Refresher 
"""
import util

'''
Stacks Are LiFo 
push -> append
pop -> delete back
'''
def stackFill(arr):
    print("Filling Stack...")
    for i in range(0,10):
        arr.append(i)
    return arr

def stackCheck(arr):
    print("Init Arr: " + str(arr))
    last = arr[-1]
    arr.pop()
    print("Removed item '%s': " % (str(last)) + str(arr))
    last = arr[-1]
    arr.pop()
    print("Removed item '%s': " % (str(last)) + str(arr))
    print("Res Arr: " + str(arr))
    return(arr)


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

    print(arr) 


def main():
    s = util.Stack()
    sFill = stackFill(s)
    sChk = stackCheck(sFill)

    q = util.Queue()
    qFill = queueFill(q)
    qChk = queueCheck(qFill)



if __name__ == "__main__":
    main()