# Brute Force

s="5347"
n=len(s)
maxi=""
for i in range(n):
    for j in range(i,n):
        sub=s[i:j+1]
        if int(sub[-1])%2==1:
            # You must handle the empty case empty string maxi.
            if maxi=="" or int(sub)>int(maxi):
                maxi=sub
print(maxi)  
# Time complecity:O(n^3) for generating all substrings and comparing them


#Time complexity: O(n^2)  still not optimal
# Better Appraoch
# start from full string and reduce len from right
# check if last digit is odd

s="5347"
n=len(s)
maxi=""

for i in range(n):
    sub=s[:n-i]
    if int(sub[-1])%2==1:
        if sub>maxi:
            maxi=sub
print(maxi)            

# Optimal approach
# Instead of checking all substrings:

# 👉 Just find rightmost odd digit
s = "534"

for i in range(len(s)-1, -1, -1):
    if int(s[i]) % 2 == 1:
        print(s[:i+1])
        break
else:
    print("")


 
