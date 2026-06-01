# 1021. Remove Outermost Parentheses
# Time complexity: O(n) where n is the length of the input string s
# Space complexity: O(n) for the result string
s="((()))"
n=len(s)
depth=0
result=""
for ch in s:
    if ch=='(':
        if depth>0:
            result+=ch
        depth+=1
    else: # )
        depth-=1
        if depth>0:
            result+=ch
print(result)    
# ✅ Rules:
# If char is (:
# If depth > 0 → add to result
# Then increase depth
# If char is ):
# Decrease depth
# If depth > 0 → add to result
# Time: O(n)
# Space: O(n) (for result)

# Approach 1: Brute Force (Conceptual)
# Idea:
# Find primitives manually
# For each:
# remove first & last char
# Concatenate
# Problem:
# Hard to detect primitives explicitly
# More complex logic
# ⛔ Not preferred