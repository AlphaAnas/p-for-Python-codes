# import hashlib
# key="I love coding in Python"
# print(hashlib.md5(key.encode()))
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j][-1]>lst[j+1][-1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst
def selection_sort(lst):
    for i in range(len(lst)):
        smallest=i
        for j in range(i+1, len(lst)):
            if lst[smallest][-1]>lst[j][-1]:
                smallest=j
        temp=lst[smallest]
        lst[smallest]=lst[i]
        lst[i]=temp
    return lst
def insertion_sort(lst):
    for i in range(len(lst)):
        j=i
        while(j>0 and lst[j-1][-1]>lst[j][-1]):
            temp=lst[j-1]
            lst[j-1]=lst[j]
            lst[j]=temp
            j-=1
    return lst
lst=["hello2",'world1', 'habib99', 'father1']
print(bubble_sort(lst),'bubble')
print(selection_sort(lst),'selection_sort')
print(insertion_sort(lst),'insertion_sort')
        



