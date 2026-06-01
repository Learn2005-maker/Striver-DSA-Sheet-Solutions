arr = [1, 2, 3]
n = len(arr)
index = -1

# Step 1: find first decreasing element from right
for i in range(n - 2, -1, -1):
    if arr[i] < arr[i + 1]:
        index = i
        break

# Step 2: if no such index found -> reverse the array
if index == -1:
    arr.reverse()
else:
    # Step 3: find element just larger than arr[index] on the right
    for i in range(n - 1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break
    # Step 4: reverse the part after index
    arr[index + 1:] = reversed(arr[index + 1:])

print(arr)
