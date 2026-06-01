def maxrowIndex(mat, n, m, col):
    maxValue = -1
    index = -1
    for i in range(n):
        if mat[i][col] > maxValue:
            maxValue = mat[i][col]
            index = i
    return index        

mat = [[10, 20, 15], 
       [21, 30, 14], 
       [7, 16, 32]]

n = len(mat)
m = len(mat[0])

low = 0
high = m - 1   # FIXED

while low <= high:
    mid = (low + high) // 2
    row = maxrowIndex(mat, n, m, mid)

    left = mat[row][mid - 1] if mid - 1 >= 0 else -1
    right = mat[row][mid + 1] if mid + 1 < m else -1

    if mat[row][mid] > left and mat[row][mid] > right:
        print(row, mid)
        break   # IMPORTANT
    elif mat[row][mid] < left:
        high = mid - 1
    else:
        low = mid + 1

# Time complexity: O(n log m)        