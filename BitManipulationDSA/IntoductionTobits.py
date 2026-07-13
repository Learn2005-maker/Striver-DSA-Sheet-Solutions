def converToBinary(n):
    rem=""
    while n>0:
        if n%2==1:
            rem+='1'
        else:
            rem+='0'
        # rem+=str(n%2)  shorter version
        n=n//2    
    rem=rem[::-1]        
    return rem
n=13
res=converToBinary(n)    
print(res)
# Time complexcity:O(logn)
# space complexcity:O(logn) 
    
  # Time complexcity:O(len(string)) 
#   space complexcity:O(1)

# def converTodecimal(string):         #  shorter version  #
#     num=0
#     for i in string:
#         num=num*2+int(i)
        
#     return num    
        
# print(converTodecimal("1101"))
       
def converTodecimal(string):
    n=len(string)
    num=0
    pow2=1
    for i in range(n-1,-1,-1):
        if string[i]=='1':
            num=num+pow2
        pow2=pow2*2
    return num
 
string="1101"
res=converTodecimal(string)    
print(res)
    
# Swap the numbers... using xor

a,b=5,6
a=a^b
b=a^b
a=a^b
print(a,b)
 
# checking if ith bit is set or not using XOR left shift
N=13
i=1
# Using xor
# 1101
if N&(1<<i)!=0:
    print(True)
else:
    print(False)
# or using right shift
N=13
i=1
if (N>>i)&1==1:
    print(True)
else:
    print(False)

# Set the ith Bit
N=13
i=2
ans=N | (1<<i)
print(ans) 

# clear the ith bit
N=13
i=2

# 1101 ---> 1001
print(bin(N & ~(1<<i))[2:])

# Toggle the ith  bit
N=13
i=2
# Toggle (reversing The bit) bits

print(bin(N^(1<<i))[2:])
