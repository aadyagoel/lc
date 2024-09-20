def BinarySearch(x, low, high, arr):
    if (low <= high):
        mid = low + (high-low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(x, mid+1, high, arr) #why does it not work without the return; it should go into an infinite loop either way right? which is why base case needed?  
        else:
            return BinarySearch(x, low, mid-1, arr)
    else:
        return -1

if __name__ == '__main__':
    arr = [90, 80, 70, 30, 10, 0]
    x = 10
    low = 0
    high = len(arr)-1
    result = BinarySearch(x, low, high, arr)
    if result!=-1:
        print(result)
    else:
        print("element not in list")
    