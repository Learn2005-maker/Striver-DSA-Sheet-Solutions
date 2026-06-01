s = "  hello   world  "

words = s.strip().split()
words.reverse()

result = " ".join(words)
print(result)
# ✅ Rules:
# 1. Trim leading and trailing spaces
# 2. Split the string into words (handle multiple spaces)
# 3. Reverse the list of words
# 4. Join the reversed list with a single space
# Time complexity: O(n) where n is the length of the input string s
# Space complexity: O(n) for the result string and the list of words
# ✅ Code (Optimal Thinking)
s = "  hello   world  "

# Step 1: clean spaces
words = s.strip().split()

# Step 2: reverse whole string (by reversing list)
words = words[::-1]

# Step 3: join
result = " ".join(words)

print(result)


# Intuition (Striver Style)
# We will:
# Traverse string from right → left
# Extract each word manually
# Add it to answer
# Maintain single space
# 👉 Why from right?
# Because we need reverse order of words

# Without split() we do manual extraction of words:
s="    hello world    "
print("String length:",len(s))
i=len(s)-1
print("Index Length",i)
res=""

while i>=0:
    # skip spaces
    while i>=0 and s[i]==" ":
        i-=1
    # 2. check if string ended    
    if i<0:
        break
    # Extract word.
    j=i
     # 3. find start of word    
    while i>=0 and s[i]!=" ":
        i-=1
    word=s[i+1:j+1]    
    if res=="":
        res+=word
    else:
        res+=" "+word
print(res)        
        
# 🔥 FULL DRY RUN (STEP BY STEP)

# Input:

# "  hello   world  "
# 🟢 Initial
# i = last index → ' '
# 🔄 Step 1: Skip spaces
# i moves left skipping ' '

# Now:

# i → 'd' (end of "world")
# 🔄 Step 2: Extract word
# j = i = 'd'

# Move left:

# d → l → r → o → w

# Stop at space

# Now:

# i → space before "world"
# 🔄 Step 3: Extract
# word = s[i+1 : j+1]

# 👉 "world"

# 🔄 Step 4: Add to result
# res = "world"
# 🔄 Step 5: Continue

# Skip spaces again

# Now:

# i → 'o' in "hello"
# 🔄 Step 6: Extract next word
# j = 'o'

# Move left:

# o → l → l → e → h

# Stop at space

# 🔄 Step 7: Extract
# word = "hello"
# 🔄 Step 8: Add
# res = "world hello"
# 🔄 Step 9: Continue

# Skip spaces → i = -1