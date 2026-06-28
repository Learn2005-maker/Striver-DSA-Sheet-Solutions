
# letter combinations of phone number
def letterCombinations(index,digits,phone,s,ans):
    if len(digits)==index:
        ans.append(s[:])
        return
    letters=phone[digits[index]]
    for ch in letters:
        letterCombinations(index+1,digits,phone,s+ch,ans)    
    

digits="23"
phone={
    "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
}
s=""
ans=[]

letterCombinations(0,digits,phone,s,ans)

print(ans)
# Time complexcity: O(3^n*n) if we ignore the 7 and 9 which have 4 letters.
# If we consider them then it will be O(4^n*n) where n is the length of the digits string .
# space complexcity: O(n) for the recursion stack