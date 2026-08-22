s = "ddaaabbca"
t = "abc"
m = len(s)

minL = float("inf")
sIndex = -1

# 1. Count the required frequencies of characters in 't'
t_count = {}
for char in t:
    t_count[char] = t_count.get(char, 0) + 1

# 2. Brute force: check every possible substring starting at index i
for i in range(m):
    dici = {}
    
    # Expand the substring ending at index j
    for j in range(i, m):
        char = s[j]
        dici[char] = dici.get(char, 0) + 1
        
        # 3. Check if current substring s[i:j+1] has all characters from 't'
        is_valid = True
        for req_char, req_count in t_count.items():
            if dici.get(req_char, 0) < req_count:
                is_valid = False
                break
                
        # 4. If it's valid, record the length and break (since any further j will just be longer)
        if is_valid:
            if (j - i + 1) < minL:
                minL = j - i + 1
                sIndex = i
            break 

# 5. Print the correct slice
if sIndex != -1:
    print(s[sIndex : sIndex + minL])
else:
    print("No valid window found")
    
    
    
    
    
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m = len(s)
        n = len(t)

        if n == 0:
            return ""

        t_mpp = {}

        for ch in t:
            t_mpp[ch] = t_mpp.get(ch, 0) + 1

        l = 0
        r = 0
        count = 0

        minL = float("inf")
        sIndex = -1

        while r < m:

            # Add s[r]
            if t_mpp.get(s[r], 0) > 0:
                count += 1

            t_mpp[s[r]] = t_mpp.get(s[r], 0) - 1

            # Window is valid
            while count == n:

                # Update answer
                if r - l + 1 < minL:
                    minL = r - l + 1
                    sIndex = l

                # Remove s[l]
                t_mpp[s[l]] += 1

                if t_mpp[s[l]] > 0:
                    count -= 1

                l += 1

            r += 1

        if sIndex == -1:
            return ""

        return s[sIndex:sIndex + minL]