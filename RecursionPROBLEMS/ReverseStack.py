def insertAtbottom(st,x):
    if not stack:
        st.append(x)
        return
    temp=st.pop()
    insertAtbottom(st,x)
    st.append(temp)
    


def reverseStack(st):
    if not st:
        return
    x=st.pop()
    reverseStack(st)
    insertAtbottom(st,x)


stack=[1,2,3,4,5]
reverseStack(stack)
print(stack)
# Time complexity: O(n^2)
# space complexity: O(n)