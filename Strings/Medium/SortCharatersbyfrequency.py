def frequencySort(self, s: str) -> str:
        dici = {}
        # Step 1: Count frequency
        for ch in s:
            dici[ch] = dici.get(ch, 0) + 1
        
        # Step 2: Sort characters
        sorted_chars = sorted(dici, key=lambda x: (-dici[x], x))
        result=""

        # Step 3: Build string using multipliaction
        for ch in sorted_chars:
            result += ch * dici[ch]

        return result

# 🔍 Dry Run
# Input:

# s = "tree"
# Step 1: Frequency Map
# t → 1  
# r → 1  
# e → 2
# Step 2: Sorting
# ['e', 'r', 't']   (because e has highest freq)
# Step 3: Build String
# "ee" + "r" + "t" = "eert"
# ⏱ Complexity
# Time: O(n log n) (sorting)
# Space: O(n) (dictionary + result)
# ⚡ Cleaner Python Way (Advanced)
# return "".join(ch * dici[ch] for ch in sorted(dici, key=lambda x: -dici[x]))

# If you want, I can also show you the optimal bucket sort approach (O(n)), which is commonly asked in interviews.