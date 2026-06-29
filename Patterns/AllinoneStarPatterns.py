# 1st Pattern
n=5
for i in range(n):
    for j in range(n):
        print('*',end="")
    print()    
print("-----")  
#2nd Pattern   
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()   
print("-----")      
# 3rd pattern    
n=5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()  
print("-----")      
# 4th Pattern

n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()    

# 5th Pattern

n=5
for i in range(n):
    for j in range(i,n):
        print('*',end="")
    print()    

# 6th Pattern

n=5
for i in range(n):
    for j in range(i+1,n+1):
        print(j,end="")
    print()    
    
# 7th pattern

n=5
for i in range(n):
    for j in range(n-i-1):
        print('-',end="")
    for j in range(2*i+1):
        print('* ',end="")
    for j in range(n-i-1):
        print('-',end="")    
    print()    
# 8th pattern
print()
print()
n=5
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print('-',end="")
    for j in range(2*i+1):
        print('* ',end="")
    for j in range(n-i-1):
        print('-',end="")    
    print()    

# 9th Pattern
print()
n=5

for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for j in range(2*i+1):
        print('*',end="")
    for j in range(n-i-1):
        print(' ',end="")    
    print()    
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(' ',end="")
    for j in range(2*i+1):
        print('*',end="")
    for j in range(n-i-1):
        print(' ',end="")    
    print()    

























    
    
    
    
    
    
    
    