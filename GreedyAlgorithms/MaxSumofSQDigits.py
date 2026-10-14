
def maxSumOfSquares(num: int, sum: int):
        if sum>9*num:
            return ""
        ans=[]
        for i in range(num):
            digit=min(9,sum)
            ans.append(str(digit))
            sum-=digit
        return "".join(ans) if sum==0 else ""