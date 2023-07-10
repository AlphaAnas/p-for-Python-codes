



def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    L=arr[:mid]
    R=arr[mid:]
    merge_sort(L)
    merge_sort(R)
    merge_two_lists(L,R,arr)
    
def merge_two_lists(L, R,arr):
    i=j=k=0
    len_a=len(L)
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
   
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i< len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j< len(R):
        arr[k]=R[j]
        j+=1
        k+=1





if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5],
        [2,9,3,345,2342,22,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)


