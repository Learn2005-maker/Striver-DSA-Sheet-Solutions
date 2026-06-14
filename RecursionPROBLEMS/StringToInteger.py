# Iterative Approach 
# Time complexcity:O(n)
# Space complexcity:O(1)
def myAtoi(s):
    sign=1
    ans=0
    started=False
    for ch in range(len(s)):
        if s[ch]==" " and not started:
            continue
        if s[ch]=="-" and not started:
            started = True
            sign=-1
            continue
        if s[ch]=="+" and not started:
            started = True
            continue
        if s[ch].isdigit():
            started=True
            ans=ans*10+int(s[ch])
        else:
            break
    ans*=sign
    if ans<-2**31:
        return -2**31
    if ans>2**31-1:
        return 2**31-1
    return ans
    
    
s="     -412345  6789293 with words 4899"

atoi=myAtoi(s)

print(atoi)

# Recursive Approach
# Time Complexcity:O(n)
# Space Complexcity:O(1)
INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s, i, num, sign):
    # Base case: end of string or non-digit
    if i >= len(s) or not s[i].isdigit():
        return sign * num

    # Update num
    num = num * 10 + int(s[i])

    # Clamp if overflow
    if sign * num <= INT_MIN: return INT_MIN
    if sign * num >= INT_MAX: return INT_MAX

    # Recurse
    return helper(s, i + 1, num, sign)

def myAtoi(s):
    i = 0

    # Skip whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1

    # Handle sign
    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Recursive helper
    return helper(s, i, 0, sign)

if __name__ == "__main__":
    s = "  -12345"
    print(myAtoi(s))  # Output: -12345

