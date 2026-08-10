nums = "1432219"
k = 3

stack = []

for digit in nums:
    while stack and k > 0 and stack[-1] > digit:
        stack.pop()
        k -= 1

    stack.append(digit)

while k > 0:
    stack.pop()
    k -= 1

res = ''.join(stack)
result=res.lstrip('0')
if res=="":
    print(0)
print(res)