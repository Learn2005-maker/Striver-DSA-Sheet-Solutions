# Back tracking
# Print N to 1 by backTrack
# Dont use num(i+1,n)
# Use num(i-1,n)
def num(i,n):
    if i<1:
        return 
    
    num(i-1,n) 
    print(i)
num(3,3)    

# Print 1 to N by backTrack
# Dont use num(i-1,n)
# Use num(i+1,n)
# Print after the function call
def num(i,n):
    if i>n:
        return
    num(i+1,n)
    print(i)
        
num(1,3)    


# Print name N times

def name(i,n):
    if i>n:
        return 0
    print("sujith") 
    
    name(i+1,n)
        
# print from N to 1
name(1,5)

def num(i,n):
    if i<n:
        return
    print(i)
    
    num(i-1,n)
num(10,1) 



# Print from 1 to N
def num(i,n):
    
    if i>n:
        return 
    print(i)
    
    num(i+1,n)
    
num(1,5)    
    
    



# using Parametizes way of summation n to 1
def summation(i,s):
    if i<1:
        print(s)
        return
    summation(i-1,s+i) 
summation(5,0)    


# sumof first n numbers using functional way

def summation(n):
    if n==0:
        return 0
    else:
        return n+summation(n-1)
n=3        
print(summation(n))     

# factorial

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=5    
print(fact(n))    



# Reversing the array
# using two pointers

def reverse(l,r):
    if l>=r:
        return
    li[l],li[r]=li[r],li[l]
    return reverse(l+1,r-1)    
    
li=[1,2,3,4,5]

l=0
r=len(li)-1

reverse(l,r)
print(li)
    
    
# using one pointer # 

def reverse(i,n):
    if i>=n/2:
        return 
    li[i],li[n-1-i]=li[n-1-i],li[i]
    return reverse(i+1,n)
    
li=[1,2,3,4,5]    
i=0
n=len(li)
reverse(i,n)
print(li)


# using for loop
li=[1,2,3,4,5] 
n=len(li)
for i in range(n//2):
    li[i],li[n-1-i]=li[n-1-i],li[i]

print(li)   



# using one pointer for palindrome recusion


def palindrome(s,i):
    n=len(s)
    if i>=n//2:
        return True
    if s[i]!=s[n-1-i]:
        return False
    
    return palindrome(s,i+1)


s="abbaabba"
i=0
print(palindrome(s,i))

    