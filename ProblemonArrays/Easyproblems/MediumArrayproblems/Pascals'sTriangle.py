# We have 3 parts in this problem
# ------------> 1 st part ---------->

# Given R and C and Tell the element at the Rth row and Cth column in the pascal triangle
# Given R and C and Tell the Rth row of the pascal triangle



# ncr=n!/(n-r)!

# Performing ncr opertaion
def generateRows(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res

r = 4
c = 2
print(generateRows(r-1,c-1))    
# Time Complexity: O(r) where r is the row number
# Space Complexity: O(1)

# <------------> 2nd part ---------->
# Given N and print the Nth Row of the pascal triangle.

def generateRows(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res


N=4

for col in range(N):
    print(generateRows(N-1,col),end=" ")
# Time Complexity: O(N* R) where N is the row number
# Space Complexity: O(1)

# Bruet Force Solution
def generateRows(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res


N=4

for col in range(N):
    print(generateRows(N-1,col),end=" ")
# Optimal Solution By figuring out the pattern or Formula of the pascal triangle


ansRow=[]

ans=1
ansRow.append(ans)
N=3
for i in range(1,N):
    ans=ans*(N-i)
    ans=ans//i
    ansRow.append(ans)

print(ansRow)    

# ------------> 3rd part ---------->
# Given N and print the first N rows of the pascal triangle.
# Brute Force Solution
# Time Complexity: O(N*N*N) where N is the number of rows
# Space Complexity: O(N^2)
def generateRows(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res    

ans = []
n = 5

for row in range(n):
    tempList = []
    for col in range(row + 1):
        tempList.append(generateRows(row, col))
    ans.append(tempList)

print(ans)




# time complexity: O(N*N) where N is the number of rows
# space complexity: O(N^2)

def generatePascal(n):
    ans = []

    for row in range(n):
        temp = []
        val = 1

        for col in range(row + 1):
            temp.append(val)

            # compute next value in O(1)
            val = val * (row - col) // (col + 1)

        ans.append(temp)

    return ans


n = 5
print(generatePascal(n))

    