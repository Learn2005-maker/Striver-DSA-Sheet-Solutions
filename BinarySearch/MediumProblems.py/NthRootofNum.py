# Using brute force approach for finding nth root of a number
# Time complexcity: O(M) space complexity: O(1)
N=3
M=27
for i in range(1,M):
    if i**N==M:
        print(i)
        break
    if i**N>M:
        print(-1)
        break
        
# using math 
root=M**(1/N)
if int(root)**N==M:
    print(int(root))
else:
    print(-1)
# Using pow fun    # 
N=4
M=625
root=pow(M,1/N)
if int(root)**N==M:
    print(int(root))
else:
    print(-1)
    
    
    # USing binary search for finding nth root of a number
N=4
M=625

low=1
high=M
ans=-1
while low<=high:
    mid=(low+high)//2
    if mid**N==M:
        ans=mid
        break
    if mid**N<M:
        low=mid+1
    else:
        high=mid-1
print(ans)        


# Time complexcity : O(log M)    



# ⚠️ But there IS a problem

# Even though no overflow happens, this line:
# mid**N
# is expensive when:
# mid is large
# N is large

# 👉 It increases time complexity unnecessarily.


# 🔥 Optimized Approach (Avoid computing full power)

# Instead of directly doing mid**N, compute it step by step and stop early.

# ✅ Efficient Power Check Function
def power(mid, N, M):
    result = 1
    for _ in range(N):
        result *= mid
        if result > M:
            return 2   # greater than M
    if result == M:
        return 1       # equal
    return 0           # less than M
# 🔹 Binary Search Using This
N = 4
M = 69

low = 1
high = M
ans = -1

while low <= high:
    mid = (low + high) // 2
    
    check = power(mid, N, M)
    
    if check == 1:
        ans = mid
        break
    elif check == 0:
        low = mid + 1
    else:
        high = mid - 1

print(ans)
# 💡 Why this is better?
# ✅ Advantages:

# Avoids unnecessary large multiplications

# Stops early when value exceeds M

# Works in languages like C++/Java (where overflow does happen)

# 🧠 Interview Insight

# Say this line 👇 and you’ll impress:

# “Instead of computing mid^N directly, I use a helper function to multiply step-by-step and stop early if it exceeds M to avoid overflow and improve efficiency.”

# ⏱ Complexity

# Binary Search: O(log M)

# Power check: O(N)
# 👉 Total: O(N log M)