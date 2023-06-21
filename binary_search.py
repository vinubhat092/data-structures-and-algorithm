def binary_search(arr,x,low,high):
    

    while low<=high:
        mid = (low + (high-low)//2)
        if x == arr[mid]:
            return mid
        if arr[mid] <x:
            low = mid+1
        else:
            high = mid -1
    return -1


arr = [2,3,5,6,7]
x = 6
data = binary_search(arr,x,0,len(arr)-1)
if data != -1:
    print("data found at", str(data))
else:
    print("data not dfount")
        