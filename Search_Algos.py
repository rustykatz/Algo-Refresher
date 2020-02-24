import random as r

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)

        i = k = j =0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        # Add residual
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1



def binarySearch(arr,n,x):
    # Only works with sorted Arr

    # l & r keep track of left and right array index
    # [0,1,2,3,4,5]
    #  ^         ^ 
    l = 0 
    r = n-1
    while l <= r: 
        mid = (l + r+1)//2

        # Check if mid of array is target
        if arr[mid] == x:
            print(f'Target Found at pos: {mid}')
            return(arr[mid])
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x: 
            l = mid + 1

def main():
    arr =[] 
    count = 0
    for i in range(20):
        num = r.randint(-100,100)
        if num not in arr:
            arr.append(num)
            count +=1
    print(f'Pre Sort Arr: {arr}')
    print(f'Count: {count}')

    # Sorting Alg
    mergeSort(arr)

    count = len(arr)
    target = arr[r.randint(1,len(arr)-1)]

    print(f'Pst Sort Arr: {arr}' )
    print(f'Target: {target}')
    
    # Search alg
    binarySearch(arr,count,target)

if __name__ == "__main__":
    main()