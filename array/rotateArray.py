#Shifting all elements by k positions, with elements that fall off one end reappearing on the other (circular shift).


#approach 1
def rotate_bruteforce(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]




#approach 2
def reverse_range(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotate_optimal(arr, k):
    n = len(arr)
    k %= n
    reverse_range(arr, 0, n - 1)      # reverse whole array
    reverse_range(arr, 0, k - 1)        # reverse first k
    reverse_range(arr, k, n - 1)          # reverse remaining n-k
    return arr



# reverse in k groups
def reverse_in_k_groups(arr, k):
    n = len(arr)
    for start in range(0, n, k):
        end = min(start + k, n) - 1
        l, r = start, end
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr