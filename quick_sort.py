# Quick Sort. [Randomized algorithm].
# 
# Case 1: Always use the first element as the pivot.
# Case 2: Always use the final element as the pivot.
# Case 3: Always use the median(middle of three) element as the pivot.


from math import ceil

count=0

def readfile(file):
    file_read=open(file,"r")
    integer_list=file_read.read().splitlines()
#Convert string list to integer list:
    integer_list = [int(i) for i in integer_list]
    file_read.close()
    return integer_list


#Choose Pivot
#Median of three pivot
def choose_pivot(arr,left,right):
    if left==right:
        return 0
    if len(arr)%2==0:
        mid=int(len(arr)/2) -1
    else:    
        mid=int(len(arr)/2)
 

    if (arr[left]-arr[mid])*(arr[left]-arr[right])<0:
        return left
    if (arr[mid]-arr[left])*(arr[mid]-arr[right])<0:
        return mid
    else: 
        return right


#Partition subroutine

def partition(arr, left, right):
    pivot=arr[left]
    i=left+1
    global count
    for j in range(i,right+1):
        if arr[j]<=pivot:
            swap(arr,j,i)
            i=i+1
        count=count+1    
    swap(arr,left,i-1)
    #print("array in partition", arr)
    return i-1

#Swap subroutine

def swap(arr, i, j):
    if i==j:
        return
    #print("i is ",i,"j is ",j)
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp


#Quick Sort

def quick_sort(arr):
    length=len(arr)
    left=0;
    right=length-1;
    if length<1:
        return arr,0

#Case 1
#    i=0
#Case 2
#   i=right
#Case 3
    i=choose_pivot(arr,left,right)

    #print("Pivot is ",i)
    #print("array in qs is ",arr)
    
    #Move the pivot to the first element.
    swap(arr,left,i)
    j=partition(arr,left,right)
    c=right-left
    #print("partition point ",j)
    arr[:j],lc=quick_sort(arr[:j])
    arr[j+1:],rc=quick_sort(arr[j+1:])
    #return arr,(count)
    return arr, (c+lc+rc)




count=0
array=[4,5,6,7,1,2,3,12]

print(array)
print(quick_sort(array))

count=0
array=[4,6,7,3,2,1,10,12,0,9]

print(array)

print(quick_sort(array))
count=0
array=[2,9,1,4]

print(array)

print(quick_sort(array))

count=0
array=readfile('QuickSort.txt')
res,countres=quick_sort(array)
print("Count",countres)
#print(res)
