def myAtoi(s):
    sign=1
    ans=0
    started=False
    for ch in range(len(s)):
        if s[ch]==" " and not started:
            continue
        if s[ch]=="-" and not started:
            started = True
            sign=-1
            continue
        if s[ch]=="+" and not started:
            started = True
            continue
        if s[ch].isdigit():
            started=True
            ans=ans*10+int(s[ch])
        else:
            break
    ans*=sign
    if ans<-2**31:
        return -2**31
    if ans>2**31-1:
        return 2**31-1
    return ans
    
    
s="     -412345  6789293 with words 4899"

atoi=myAtoi(s)

print(atoi)

