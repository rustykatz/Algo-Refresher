# Basic Sorting Algorithms
import random
import time
# 1) Bubble Sort
# Time Complexity WORST CASE - 0(n^2)
#   -> When array is reverse sorted
# Time Complexity AVERAGE CASE - 0(n^2)
# Time Complexity BEST CASE - 0(n) **with boolean modifier
#   -> Array is already sorted.
#   -> NEED TO USE A BOOLEAN TO CHECK IF SWAPPED
# Iterates through the entire array and swaps elem with next if
# next elem is smaller.
# Every pass at least sorts the last item in array


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped == False:
            break
    return arr


# 2) Merge Sort
# Time Complexity WORSE, AVERAGE, BEST CASE - 0(nlogn)
#   -> divides array regardless if sorted already or not
#  Steps: 1. Find mid array
#         2. Call msort on first half
#         3. Call msort on second half
#         4. Combine halves


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    res = []
    mid = len(arr) // 2  # use floor division to round down
    L = arr[:mid]  # Left side up start to mid
    R = arr[mid:]  # Right side from mid to end

    mergeSort(L)  # Sort Left
    mergeSort(R)  # Sort Right

    # COMBINE HALVES - note halves may not be same len
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1

    while i < len(L):
        res.append(L[i])
        i += 1

    while j < len(R):
        res.append(R[j])
        j += 1
    return res

# 3) Insertion Sort
# Time Complexity WORST CASE - 0(n^2)
#   -> Reverse sorted
# Time Complexity AVERAGE CASE - 0(n^2)
# Time Complexity BEST CASE - 0(n)
#   -> No Swaps
# Steps: 1. loop from 1 to (n-1)
#        2. if i < i-1 shift everything up until you find insertion spot


def insertionSort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
    return arr

# 4) Quick Sort
# Time Complexity WORST CASE - 0(n^2)
#   -> Pivot is always largest or smallest elem
# Time Complexity AVERAGE CASE - 0(nlogn)
# Time Complexity BEST CASE - 0(nlogn)
#   -> Occurs when middle is always picked as pivot
# Steps: 1. Pick a pivot
#        2. Place smaller than pivot left, bigger right

# Gets pivot and places in correct position in sorted array
# Smaller items go to left of pivot, bigger to the right


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i] = arr[j]
            arr[j] = arr[i]

    arr[i+1] = arr[high]
    arr[high] = arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

    return arr

# 5) Heap Sort


def printError(name, unsortedArr, key, sort):
    print(
    "ERROR " + name + '\n' +
    "Arr  -> " + str(unsortedArr) + '\n' +
    "Key  -> " + str(key) + '\n' +
    "Sort -> " + str(sort)
    )


def main():
    # INIT
    num_tests = 1000
    bsort_avg_time = 0
    bsort_passed = 0

    msort_avg_time = 0
    msort_passed = 0

    isort_avg_time = 0
    isort_passed = 0

    qsort_avg_time = 0
    qsort_passed = 0

    heapsort_avg_time = 0
    heapsort_passed = 0

    for _ in range(num_tests):
        # Create & populate test array
        testArr = []
        for elem in range(10):
            testArr.append(random.randint(1, 100))
        # KEY
        unsortedArr = testArr
        key = sorted(testArr)

        # Call Sorting Algs
        # Bubble Sort
        bsort_time_start = time.time_ns()
        bsort = bubbleSort(testArr)
        bsort_time_end = time.time_ns()
        bsort_avg_time += (bsort_time_end - bsort_time_start)

        if bsort == key:
            bsort_passed += 1
        else:
            name = "Bubble Sort"
            printError(name, unsortedArr, key, bsort)

        # Merge Sort
        msort_time_start = time.time_ns()
        msort = mergeSort(testArr)
        msort_time_end = time.time_ns()
        msort_avg_time += msort_time_end - msort_time_start

        if msort == key:
            msort_passed += 1
        else:
            name = "Merge Sort"
            printError(name, unsortedArr, key, msort)

        # Insertion Sort
        isort_time_start = time.time_ns()
        isort = insertionSort(testArr)
        isort_time_end = time.time_ns()
        isort_avg_time += isort_time_end - isort_time_start

        if isort == key:
            isort_passed += 1
        else:
            name = "Insertion Sort"
            printError(name, unsortedArr, key, isort)


        # Quick Sort
        qsort_time_start = time.time_ns()
        qsort = quickSort(testArr, 0, len(testArr) - 1)
        qsort_time_end = time.time_ns()
        qsort_avg_time = qsort_time_end - qsort_time_start

        if qsort == key:
            qsort_passed += 1
        else:
            name = "Quick Sort"
            printError(name, unsortedArr, key, qsort)

        # # Selection Sort
        # heapsort_time_start = time.time()
        # heapsort = selectionSort(testArr)
        # heapsort_time_end = time.time()
        # heapsort_avg_time = heapsort_time_end - heapsort_time_start

        # if heapsort == key:
        #     heapsort_passed += 1

    print("%d / %d Bubble Sort test cases passed in '%d' ns!" %
        (bsort_passed, num_tests, (bsort_avg_time / num_tests)))

    print("%d / %d Merge Sort test cases passed in '%d' ns!" %
        (msort_passed, num_tests, (msort_avg_time / num_tests)))

    print("%d / %d Insertion Sort test cases passed in '%d' ns!" %
        (isort_passed, num_tests, (isort_avg_time / num_tests)))

    print("%d / %d Quick Sort test cases passed in '%d' time!" %
        (qsort_passed, num_tests, (qsort_avg_time / num_tests)))

    # print("%d / %d Selection Sort test cases passed in '%d' time!" %
    #     (heapsort_passed, num_tests, (heapsort_avg_time / num_tests)))

main()
