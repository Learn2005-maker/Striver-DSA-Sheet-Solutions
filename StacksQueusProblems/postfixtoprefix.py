def postfix_to_prefix(exp):
    stack=[]
    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            t1=stack.pop()
            t2=stack.pop()
            convertedstr=ch+t2+t1
            stack.append(convertedstr)
    return stack[-1]
    
exp = "AB+CD-*"
print(f"Postfix: {exp}")
print(f"Prefix:  {postfix_to_prefix(exp)}")




