def BinarySearch(x, low, high, arr):
    while(low <= high):
        mid = low + (high-low)//2 
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            high = mid - 1
        else:
            low = mid + 1
    return -1 

if __name__ == '__main__':
    arr = [10, 9, 8, 7, 3, 0]
    x = 3
    low = 0
    high = len(arr)-1
    result = BinarySearch(x, low, high, arr)
    if result != -1:
        print(result)
    else:
        print("element not found")

#low, high labelling is context dependent on the indices not values 
