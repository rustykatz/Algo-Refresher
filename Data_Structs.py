"""
Python Data Struct Refresher 
"""
import util

'''
Stacks Are LiFo 
Support: push(), pop()
'''
def stackFill(arr):
    for i in range(0,10):
        arr.append(i)

    return arr

def stackCheck(arr):
    print("Init Arr: " + str(arr))
    last = arr[-1]
    arr.pop()
    print("Removed last item '%s': " % str(last) + str(arr))
    arr.pop(5)
    print("Removing key -> 5: " + str(arr))
    print("Res Arr: " + str(arr))
    return arr


'''
Queues are FiFo
Support: put(), get()
'''
def queueFill(arr):
    for i in range(10):
        arr.push(i)
        
    return arr

def queueCheck(arr):
    print("Init Arr: " + str(arr))
    arr.pop()
    print(arr) 


def main():
    #arr =[]
    # sFill = stacks(arr)
    # sChk = stackCheck(sFill)

    q = util.Queue()
    qFill = queueFill(q)
    qChk = queueCheck(qFill)



if __name__ == "__main__":
    main()