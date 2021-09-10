# Divide and Conquer Algorithm for Counting Inversions.
# 

from math import ceil

def readfile(file):
    file_read=open(file,"r")
    integer_list=file_read.read().splitlines()
#Convert string list to integer list, else number of inversions will be wrong.
    integer_list = [int(i) for i in integer_list]
    file_read.close()
    return integer_list

# Merge two sub arrays
# Count inversions according to Lemma 3.1 (Algorithms Illuminated book)
def merge_array(left_array, right_array):
    
    llen=len(left_array)
    rlen=len(right_array)

    lidx=0
    ridx=0
    aidx=0
    count_inv=0

    array=[0]*(llen+rlen)

    while lidx<llen and ridx<rlen:
        if left_array[lidx]<=right_array[ridx]:
            array[aidx]=left_array[lidx]
            lidx+=1
            aidx+=1
        else:
            array[aidx]=right_array[ridx]
            ridx+=1
            aidx+=1
            count_inv+=(llen-lidx)
    
    while lidx<llen:
            array[aidx]=left_array[lidx]
            lidx+=1
            aidx+=1
            
    while ridx<rlen:
            array[aidx]=right_array[ridx]
            ridx+=1
            aidx+=1

    return (array,count_inv)


#Merge Sort and Count inversions.
def merge_sort(arr):
    if len(arr)<=1:
        return arr,0

    n=len(arr)
    m=ceil(n/2)
    
    left_array,left_inv=merge_sort(arr[:m])
    right_array,right_inv=merge_sort(arr[m:])
    
    sorted_array,count_inv=merge_array(left_array,right_array)

    return (sorted_array,count_inv+left_inv+right_inv)

array=[4,5,6,7,1,2,3,12]
sorted,count_inv=merge_sort(array)

print(sorted)
print(count_inv)

array=[0,1,3,5,2,4,6]
sorted,count_inv=merge_sort(array)

print(sorted)
print(count_inv)



array=[1,7,3,4,5,8,2]
sorted,count_inv=merge_sort(array)

print(sorted)
print(count_inv)


array=[1000000,100000,10000,1000,100,10,1]
sorted,count_inv=merge_sort(array)

print(sorted)
print("10s",count_inv)


array=[3,1,9,3,2,1]
sorted,count_inv=merge_sort(array)

print(sorted)
print(count_inv)

array=readfile('IntegerArray.txt')
#print(array)
sorted,count_inv=merge_sort(array)

#print(sorted)
print(count_inv)
print(len(array))
