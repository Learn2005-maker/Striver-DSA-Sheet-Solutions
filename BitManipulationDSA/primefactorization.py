# Interview Approach
# def isPrime(n):
#     if n <= 1:
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True
# print(isPrime(13))    

def prime(n):
    if n<=1:
        return False
    count=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            count+=1
            if i!=n//i:
                count+=1
            if count>2:
                break
    return count == 2 
lis=[]
n=60
for i in range(2,n+1):
    if n%i==0:
        if prime(i):
            lis.append(i)
print(lis)            
# Time complexcity:O(N*sqrt(n))


def prime(n):
    if n<=1:
        return False
    count=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            count+=1
            if i!=n//i:
                count+=1
            if count>2:
                break
    return count == 2 
n=60  
lis=[]
for i in range(1,int(n**0.5)+1)    :
    if n%i==0:
        if prime(i):
            lis.append(i)
            if i!=n//i:
                if prime(n//i):
                    lis.append(n//i)
print(lis)      


# Optimal approch  . while we doing maths school division
n=3
lis=[]
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        lis.append(i)
        # again divide it as many times as possible
        while n%i==0:
            n=n//i
# if they given as prime only like n=37
if n!=1:
    lis.append(n)            
print(lis)       

# time complexcity:O(sqrt(n)*logn (for division))
# space: depending on prime factors