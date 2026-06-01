class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            s1=expand(i,i)
            s2=expand(i,i+1)  
            res=max(res,s1,s2,key=len)   
        return res                    
s="babad"
print(Solution().longestPalindrome(s))       