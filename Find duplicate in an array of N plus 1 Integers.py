numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):
  
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size
  
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")
