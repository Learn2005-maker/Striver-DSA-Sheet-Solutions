# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
# brute force approach: Generate all possible rotations of s and check if any of them matches goal.
def rotateString(s,goal):
    if len(s)!=len(goal):
        return False
    temp=s
    for _ in range(len(s)):
        temp=temp[1:]+temp[0]
        if temp==goal:
            return True
    return False


s="abcde"    
goal="cdeab"

print(rotateString(s,goal))

# Optimal Approach: Concatenate s with itself and check if goal is a substring of the concatenated string. 
# This works because if goal is a rotation of s, it will be found in s+s.
def rotateString(s,goal):
    if len(s)!=len(goal):
        return False
    return goal in (s+s)


s="abcde"    
goal="cdeab"

print(rotateString(s,goal))