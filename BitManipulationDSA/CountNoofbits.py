# Count the Number of Set Bits
n = 5
cnt = 0

while n > 0:
    if n % 2 == 1:
        cnt += 1
    n = n // 2
print(cnt)  

# Using Bit manipulation

n=5
count=0
while n>0:
    if n&1:
        count+=1
    n=n>>1
print(count)    


# Brian Kernighan's Algorithm) Most Efficient

n=5
cnt=0

while n!=0:
    cnt+=1
    n=n&(n-1)
print(cnt)    

# Method 1 (% 2): O(number of bits) ≈ O(log n)
# Method 2 (& 1): O(number of bits) ≈ O(log n)
# Method 3 (n & (n - 1)): O(number of set bits), 
# which is often faster than O(log n) when the number has few set bits.

