class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        # Copy next node value
        node.val = node.next.val

        # Skip next node
        node.next = node.next.next


# Creating Linked List
head = ListNode(4)
second = ListNode(5)
third = ListNode(1)
fourth = ListNode(9)

head.next = second
second.next = third
third.next = fourth


# Function to print linked list
def print_ll(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


print("Before Deletion:")
print_ll(head)

# Delete node 5
sol = Solution()
sol.deleteNode(second)

print("After Deletion:")
print_ll(head)