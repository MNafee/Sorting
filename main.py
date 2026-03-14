import Sorting
import matplotlib.pyplot as plt
import random


def generateRandomArray(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 100000))
    return list


def main():
    # Part II tests
    list = [2,1,6,2,5,6,7,22,41,21,12,13,14,15]
    print("Original array:", list)
    print("3rd smallest element:", Sorting.kthSmallest(0, len(list) - 1, 3, list))
    print("Hybrid Merge Sort:")
    cpy = list[:]
    Sorting.HybridMergeSort(cpy, 0, len(cpy) - 1,4)
    print("Sorted array:", cpy,end="\n\n")

    # Part I
    sizes = [100, 500, 1000, 5000, 10000, 25000]# 50000, 100000]
    bubble_times = []
    selection_times = []
    insertion_times = []
    merge_times = []
    quick_times = []
    heap_times = []

    for size in sizes:
        arr = generateRandomArray(size)
        print(f"Sorting array of size {size}...")
        bubble_times.append(Sorting.BubbleSort(arr.copy())[0])
        selection_times.append(Sorting.SelectionSort(arr.copy())[0])
        insertion_times.append(Sorting.InsertionSort(arr.copy())[0])
        merge_times.append(Sorting.MergeSortTimer(arr.copy())[0])
        quick_times.append(Sorting.QuickSortTimer(arr.copy())[0])
        heap_times.append(Sorting.heapSortTimer(arr.copy())[0])

    print("Done")

    print("Bubble sort times:", bubble_times)
    print("Selection sort times:", selection_times)
    print("Insertion sort times:", insertion_times)
    print("Merge sort times:", merge_times)
    print("Quick sort times:", quick_times)
    print("Heap sort times:", heap_times)

    plt.figure()
    plt.plot(sizes, bubble_times, label='Bubble Sort',marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort',marker='o')
    plt.plot(sizes, insertion_times, label='Insertion Sort',marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort',marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort',marker='o')
    plt.plot(sizes, heap_times, label='Heap Sort',marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (ms)')
    plt.legend()
    
    plt.figure()
    plt.plot(sizes, merge_times, label='Merge Sort',marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort',marker='o')
    plt.plot(sizes, heap_times, label='Heap Sort',marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.show()

    




if __name__ == "__main__":
    main()