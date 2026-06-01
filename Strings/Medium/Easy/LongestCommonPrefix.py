# 14. Longest Common Prefix
# Brute Force Approach
# Compare characters of all strings one by one until a mismatch is found.
# Time complexity: O(M*N) where M is the length of the longest common prefix and N is the number of strings.
def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for s in strs:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]
# Better Approach
# Sort the strings and compare the first and last strings.
# Time complexity: O(M*N*log(N)) where M is the length of the longest common prefix and N is the number of strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]

    i = 0
    while i < len(first) and first[i] == last[i]:
        i += 1

    return first[:i]
# Optimal Approach
# Use the first string as a reference and iteratively reduce the prefix until it matches all strings.
# Time complexity: O(M*N) where M is the length of the longest common prefix and N is the number of strings.

def longestCommonPrefix(strs):
    prefix = strs[0]

    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix