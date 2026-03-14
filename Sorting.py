import time
from random import randint
from random import shuffle

#---------------------------------------------------------- Bubble Sort ----------------------------------------------------------
def BubbleSort(arr):
    startTime = time.time()
    n = len(arr)
    flag = True;
    for i in range(n):
        flag  = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return ((time.time() - startTime) * 1000,arr)

#---------------------------------------------------------- Selection Sort ----------------------------------------------------------
def SelectionSort(arr):
    startTime = time.time()
    n = len(arr)

    for i in range(1, n):
        minn = i-1
        for j in range(i, n):
            if arr[j] < arr[minn]:
                #arr[i - 1], arr[j] = arr[j], arr[i - 1]
                minn = j
        arr[i - 1], arr[minn] = arr[minn], arr[i - 1]
    return ((time.time() - startTime) * 1000,arr)

#---------------------------------------------------------- Insertion Sort ----------------------------------------------------------
def InsertionSort(arr):
    startTime = time.time()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return ((time.time() - startTime) * 1000, arr)

#---------------------------------------------------------- Merge Sort ----------------------------------------------------------
def MergeSortTimer(arr):
    startTime = time.time()
    MergeSort(arr, 0, len(arr) - 1)
    return ((time.time() - startTime) * 1000, arr)

def MergeSort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    MergeSort(arr, l, mid)
    MergeSort(arr, mid + 1, r)
    res = []
    pointer_l, pointer_r = l, mid + 1
    while pointer_l <= mid and pointer_r <= r:
        if arr[pointer_l] < arr[pointer_r]:
            res.append(arr[pointer_l])
            pointer_l += 1
        else:
            res.append(arr[pointer_r])
            pointer_r += 1

    while pointer_l <= mid:
        res.append(arr[pointer_l])
        pointer_l += 1

    while pointer_r <= r:
        res.append(arr[pointer_r])
        pointer_r += 1

    for i in range(r - l + 1):
        arr[l + i] = res[i]

#---------------------------------------------------------- Quick Sort ----------------------------------------------------------

def QuickSortTimer(arr):
    startTime = time.time()
    QuickSort(0, len(arr) - 1, arr)
    return ((time.time() - startTime) * 1000, arr)

def partition(low, high, arr):
	piv = low + randint(0, high - low)
	arr[piv], arr[low] = arr[low], arr[piv]
	i = low
	
	for j in range(low + 1, high + 1):
		if arr[j] <= arr[low]:
			i = i + 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[i], arr[low] = arr[low], arr[i]
	return i

def QuickSort(low, high, arr):
	if low < high:
		p = partition(low, high, arr)
		QuickSort(low, p - 1, arr)
		QuickSort(p + 1, high, arr)

#---------------------------------------------------------- Kth Smallest Element ----------------------------------------------------------
def kthSmallest(low, high, k, arr):
	if low == high:
		return arr[low]
	if low > high or k > high - low + 1:
		return -1
	p = partition(low, high, arr)
	if p - low + 1 == k:
		return arr[p]
	if p - low + 1 > k:
		return kthSmallest(low, p - 1, k, arr)
	return kthSmallest(p + 1, high, k - (p - low + 1), arr)

#---------------------------------------------------------- Heap Sort ----------------------------------------------------------
def maxHeapify(i, n, arr):
	lt = i * 2 + 1
	rt = i * 2 + 2
	mx = i #find maximum child
	if lt < n and arr[lt] > arr[mx]:
		mx = lt
	if rt < n and arr[rt] > arr[mx]:
		mx = rt
	if mx != i:
		arr[i], arr[mx] = arr[mx], arr[i]
		maxHeapify(mx, n, arr)

def buildMaxHeap(arr):
	n = len(arr)
	for i in range((n - 1) // 2, -1, -1):
		maxHeapify(i, n, arr)
	return arr

def heapSort(arr):
	arr = buildMaxHeap(arr)
	n = len(arr)
	for i in range(0, n):
		#pop largest element
		arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]
		maxHeapify(0, n - i - 1, arr)
	return arr
		

def heapSortTimer(arr):
    startTime = time.time()
    heapSort(arr)
    return ((time.time() - startTime) * 1000, arr)




def HybridMergeSort(arr , l, r, threshold = 6): # this could've just been added to the merge function, its just an extra if condition
    #print(l , r)                               # But 
    if l >= r:
        return
    if r - l + 1 <= threshold:
        print("selection sort",l,r)
        arr[l:r+1] = SelectionSort(arr[l:r+1])[1]
        return
    print("merge sort",l,r)
    mid = (l + r) // 2
    HybridMergeSort(arr, l, mid, threshold)
    HybridMergeSort(arr, mid + 1, r, threshold)
    res = []
    pointer_l, pointer_r = l, mid + 1
    while pointer_l <= mid and pointer_r <= r:
        if arr[pointer_l] < arr[pointer_r]:
            res.append(arr[pointer_l])
            pointer_l += 1
        else:
            res.append(arr[pointer_r])
            pointer_r += 1

    while pointer_l <= mid:
        res.append(arr[pointer_l])
        pointer_l += 1

    while pointer_r <= r:
        res.append(arr[pointer_r])
        pointer_r += 1

    for i in range(r - l + 1):
        arr[l + i] = res[i]
      


if __name__ == "__main__": # for our testing, for actual stuff, go to main.py
    list = [64, 34, 25, 12, 22, 11, 90,1,1,1,1,1]

    print("Original array:", list)
    cpy = list[:]
    HybridMergeSort(cpy, 0, len(cpy) - 1)
    print("Hybrid sort array:", cpy)
    cpy = list[:]
    print("Heap zeft",heapSort(cpy))
    # BubbleSort
    cpy = list[:]
    startTime = time.time()
    BubbleSort(cpy)
    bubble_delta_time = (time.time() - startTime) * 1000

    # SelectionSort:
    cpy = list[:]
    startTime = time.time()
    print(cpy)
    SelectionSort(cpy)
    print("selection",cpy)
    select_delta_time = (time.time() - startTime) * 1000

    # MergeSort:
    cpy = list[:]
    startTime = time.time()
    MergeSort(cpy, 0, len(cpy) - 1)
    merge_delta_time = (time.time() - startTime) * 1000

    # QuickSort:
    cpy = list[:]
    startTime = time.time()
    cpy = QuickSort(0, len(cpy) - 1,cpy)
    quick_delta_time = (time.time() - startTime) * 1000

    print("Time taken for Bubble Sort:", bubble_delta_time, "milliseconds")
    print("Time taken for Selection Sort:", select_delta_time, "milliseconds")
    print("Time taken for Merge Sort:", merge_delta_time, "milliseconds")
    print("Time taken for Quick Sort:", quick_delta_time, "milliseconds")
    
    
