# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

s="aabcb"
n=len(s)
total=0
for i in range(n):
    freq=[0]*26
    for j in range(i,n):
        freq[ord(s[j])-ord('a')]+=1
        maxf=max(freq)
        minif=min(f for f in freq if f>0)
        
        total+=maxf-minif
print(total)