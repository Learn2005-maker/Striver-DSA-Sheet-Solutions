# Reverse an Integer
# You are given a signed 32-bit integer x. You need to return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.1st
# 1st way
x=1234

rev_num=str(x)[::-1]
print(int(rev_num))


# 2nd Way
x=-123
sign=-1 if x<0 else 1 # here we handle sign separately #step 1
x=abs(x) #convert to positive # step 2
rev=0

while x:
    digit=x%10
    rev=rev*10+digit
    x=x//10
rev=sign*rev # step 3    

if rev<-2**31 or rev>2**31-1:
    print(0)
else:    
    print(rev)    
