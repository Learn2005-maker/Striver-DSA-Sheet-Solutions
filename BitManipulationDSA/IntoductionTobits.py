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
    
    
    
    
            
                       
            