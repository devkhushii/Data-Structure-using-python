# Cyclic Sort

# For arrays containing values 1..n (or 0..n-1) with possible duplicates/missing values, cyclic sort places each value at its "correct" index in O(n) time using swaps, without extra space.

def cyclicSort(arr):
    n=len(arr)
    i=0
    while i<n:
        correct_idx=arr[i]-1
        if arr[i]!=arr[correct_idx]:
            arr[i],arr[correct_idx]=arr[correct_idx],arr[i]
        else:
            i+=1
    return arr

print(cyclicSort([1,7,2,3,4,1,5,6]))