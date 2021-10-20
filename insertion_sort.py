#Insertion Sort


def insertion_sort(arr):


    for i in range(1,len(arr)):
        key=arr[i]

        for j in range(0,i):
            if (arr[j]>arr[i]):
                (arr[j],arr[i])=(arr[i],arr[j])

    return arr



arr=[5,6,4,7,9,1]

print(insertion_sort(arr))

arr=[4,5,6,7,1,2,3,12]
print(insertion_sort(arr))     

arr=[1,2,3,4,5,6,7,100,99,89,56,34,45,67]
print(insertion_sort(arr))

