
# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called its divisor.


n=6
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(factors)  # Output: [1, 2, 3, 6]        