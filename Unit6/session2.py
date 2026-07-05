# Problem 5: Add Two Numbers Represented by Linked Lists
### Understand
# 1. Share 2 questions you would ask to help understand the question:
# Are the linked lists guaranteed to have the same length?
# Should I return a new linked list or modify one of the existing ones?

### Plan
# 2. Write out in plain English what you want to do:
# I will iterate through both linked lists simultaneously, adding corresponding values along with any carry from the previous addition.
# I will create a new linked list to store the result.

## 3. Translate each sub-problem into pseudocode:
# Initialize a dummy node to help build the result list.
# Initialize a carry variable to 0.
# While there are still nodes in either list or there is a carry:
#     Get the values from the current nodes of both lists (or 0 if the node is None).
#     Calculate the sum of the two values and the carry.
#     Update the carry for the next iteration (sum // 10).
#     Create a new node with the value of (sum % 10) and append it to the result list.
#    Move to the next nodes in both lists (if they exist).

#### Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it is a common interview question that tests understanding of linked lists and 
# basic arithmetic operations. It also helps practice creating new linked list nodes and managing carry values.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    current = dummy
    carry = 0

    while head_a or head_b or carry:
        val_a = head_a.value if head_a else 0
        val_b = head_b.value if head_b else 0

        total = val_a + val_b + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next

        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next

    return dummy.next

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5

head_a = Node(2, Node(4, Node(3)))
head_b = Node(5, Node(6, Node(4)))
sum = add_two_numbers(head_a, head_b)
print(sum.value)

# Problem 6: Reverse a sublist of a Linked List
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should I reverse the linked list in place or create a new list?
# What should I return if m and n are the same?

### P - Plan
# 2. Write out in plain English what you want to do:
# I would walk through the list and reverse the pointers between the m-th and n-th nodes
# I would keep track of the previous node, the current node, and the next node so I do not lose the rest of the list.

# 3. Translate each sub-problem into pseudocode:
# Start with previous as None and current as the head.
# Move previous to the (m-1)-th node and current to the m-th node
# Save the next node, reverse the current pointer, and move both pointers forward until reaching the n-th node.
# Return the head of the modified list.

# ### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because reversing a sublist of a linked list is a common interview question.
# It helped me practice updating pointers carefully without breaking the list.

def reverse_between(head, m, n):
    if not head or m == n:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next

    current = prev.next
    
    for _ in range(n - m):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

# input list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
reversed_head = reverse_between(head, 2, 5)
current = reversed_head
print()
while current:
    print(current.value)
    current = current.next

# Problem 3 Problem set 2: Delete Duplicates in a Linked List
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should I remove all duplicates or just the extra occurrences?
# What should I return if the list is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# I would walk through the list and check if the current node's value is the same as the next node's value.
# If it is, I would skip the next node by changing the current node's next pointer to the next node's next pointer.
# I would continue this process until I reach the end of the list.

# 3. Translate each sub-problem into pseudocode:
# Start with current as the head.
# While current and current.next are not None:
#     If current.value is equal to current.next.value:
#         Skip the next node by setting current.next to current.next.next
#     Else:
#        Move current to the next node.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it is a common interview question that tests understanding of linked lists 
# and how to manipulate pointers. It also helps practice iterating through a list and conditionally modifying it.

def delete_dupes(head):
    if not head:
        return head

    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head

head = Node(1, Node(1, Node(2, Node(3, Node(3)))))
current = head
while current:
    print(current.value)
    current = current.next
print()
delete_dupes(head)
current = head
while current:
    print(current.value)
    current = current.next