# Brute Force Approach
# Time Complexity: O(n*m log(n*m))+O(n*m) for sorting the 1D array
matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 

n=len(matrix)
m=len(matrix[0])
sort_1d_array=[]
for i in range(n):
    for j in range(m):
        sort_1d_array.append(matrix[i][j])
sort_1d_array.sort()
index=(n*m//2)
print(sort_1d_array[index])


# optimal using binary search
def upperBound(arr, n, x):
    ans = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def countSmallerEquals(matrix, n, m, x):
    count = 0
    for i in range(n):
        count += upperBound(matrix[i], m, x)
    return count


def matrixMedian(matrix, n, m):
    low = float("inf")
    high = float("-inf")

    # find min and max
    for i in range(n):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][m - 1])

    req = (n * m) // 2

    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallerEquals(matrix, n, m, mid)

        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low


# Test
matrix = [[1, 4, 9],
          [2, 5, 6],
          [3, 7, 8]]

n = len(matrix)
m = len(matrix[0])

print(matrixMedian(matrix, n, m))