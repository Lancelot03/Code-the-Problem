def binary_search(arr, low, high, x):

# Check base case
if high >= low:

    mid = (high + low) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)

else:
    return -1
arr = [ 15, 3, 4, 10, 40 ]
x = 1

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
return("Element is present at index", str(result))
else:
return("Element is not present in array")

