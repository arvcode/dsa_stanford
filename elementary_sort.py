#Insertion Sort & Selection sort
 
# Compare elements with its predecessors and move it.

def insertion_sort(arr):


    for i in range(1,len(arr)):
        key=arr[i]

        for j in range(0,i):
            if (arr[j]>arr[i]):
                (arr[j],arr[i])=(arr[i],arr[j])

    return arr


def selection_sort(arr):

    for i in range(0,len(arr)):
        low=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                low=j
                (arr[low],arr[i])=(arr[i],arr[low])

    return arr


print("Insertion sort")
arr=[5,6,4,7,9,1]

print(insertion_sort(arr))

arr=[4,5,6,7,1,2,3,12]
print(insertion_sort(arr))     

arr=[1,2,3,4,5,6,7,100,99,89,56,34,45,67]
print(insertion_sort(arr))

print("Selection sort")
arr=[5,6,4,7,9,1]
print(selection_sort(arr))

arr=[4,5,6,7,1,2,3,12]
print(selection_sort(arr))

arr=[1,2,3,4,5,6,7,100,99,89,56,34,45,67]
print(selection_sort(arr))

arr=[10,9,8,7,6,5,4,3,2,1]
print(selection_sort(arr))
