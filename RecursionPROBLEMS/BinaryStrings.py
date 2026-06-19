def generate(n,s=""):
    if len(s)==n:
        print(s)
        return
    
    generate(n,s+"0")
    if  not s or s[-1]!='1':
        generate(n,s+"1")

generate(3)
# time complexity: O(2^n)
# Also, space complexity: O(n) for the recursion stack