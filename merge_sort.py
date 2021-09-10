#Merge Sort algorithm.

from math import ceil

def merge_array(left_array, right_array):
    
    llen=len(left_array)
    rlen=len(right_array)

    lidx=0
    ridx=0
    aidx=0

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
    
    while lidx<llen:
            array[aidx]=left_array[lidx]
            lidx+=1
            aidx+=1
    while ridx<rlen:
            array[aidx]=right_array[ridx]
            ridx+=1
            aidx+=1

    return array



def merge_sort(arr):
    if len(arr)<=1:
        return arr

    n=len(arr)
    m=ceil(n/2)
    
    left_array=merge_sort(arr[:m])
    right_array=merge_sort(arr[m:])
    
    sorted_array=merge_array(left_array,right_array)

    return sorted_array

array=[4,5,6,7,1,2,3,12]
sorted=merge_sort(array)

print(sorted)