# Time complecity: O(nlogn) due to sorting
def Anagram(s,t):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)
    
# time complexity: O(n) using hash map
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    
    return True


s = "anagram"
t = "nagaram"
print(Anagram(s,t))
print(isAnagram(s,t))