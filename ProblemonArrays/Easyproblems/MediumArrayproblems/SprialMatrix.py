matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

r = len(matrix)
c = len(matrix[0])

left = 0
right = c - 1
top = 0
bottom = r - 1

ans = []

while top <= bottom and left <= right:

    # left → right
    for i in range(left, right + 1):
        ans.append(matrix[top][i])
    top += 1

    # top → bottom
    for i in range(top, bottom + 1):
        ans.append(matrix[i][right])
    right -= 1

    # right → left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1

    # bottom → top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1

print(ans)
