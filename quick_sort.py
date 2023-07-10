


def swap(a, b , arr):
    tmp=arr[a]
    arr[b]=arr[a]
    arr[a]=arr[b]
def quick_sort(arr,start, end):
    if start<end:
        pi=partition(arr, start,end)
        #left partition 
        quick_sort(arr, 0,pi-1)
        #right partition
        quick_sort(arr, pi+1,end)

def partition(arr,start, end):
    # pivot_index=0
    # pivot=arr[0]
    pivot_index = start
    pivot = arr[pivot_index]
    
    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            swap(start, end,arr)
    swap(pivot_index, end, arr)
    return end




# if __name__ == '__main__':
#     elements = [11,9,29,7,2,15,28]
#     # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
#     quick_sort(elements, 0, len(elements)-1)
#     print(elements)

#     tests = [
#         [11,9,29,7,2,15,28],
#         [3, 7, 9, 11],
#         [25, 22, 21, 10],
#         [29, 15, 28],
#         [],
#         [6]
#     ]

#     for elements in tests:
#         quick_sort(elements, 1, len(elements)-1)
#         print(f'sorted array: {elements}')


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5],
       
    ]

    for arr in test_cases:
        quick_sort(arr,1, len(arr)-1)
        print(arr)
    arr=[2,9,3,345,2342,22,5]
    quick_sort(arr,1,len(arr)-1)
    print(f'sorted array is :{arr}')
