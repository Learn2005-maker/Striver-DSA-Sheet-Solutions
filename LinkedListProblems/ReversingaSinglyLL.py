class Solution:
    # class ListNode:
    #     def __init__(self, data):
    #         self.data = data
    #         self.prev = None
    #         self.next = None

    def reverseDLL(self, head):

        if head is None:
            return None

        stack = []

        temp = head

        # push all node data into stack
        while temp:
            stack.append(temp.data)
            temp = temp.next

        temp = head

        # replace data using stack
        while temp:
            temp.data = stack.pop()
            temp = temp.next

        return head
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            front = curr.next

            curr.next = prev

            prev = curr

            curr = front
        return prev    