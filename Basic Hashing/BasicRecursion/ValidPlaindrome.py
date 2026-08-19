
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
def is_palindrome(s):
    result=[]
    for ch in s:
        if ch.isalnum():
            low=ch.lower()
            result.append(low)
    res="".join(result)
    return res[::-1]==res

s = "A man, a plan, a canal: Panama"
result=[]

print(is_palindrome(s))


