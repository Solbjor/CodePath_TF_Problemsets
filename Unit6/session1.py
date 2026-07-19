# Problem 4: Find the Middle
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Is the linked list guaranteed to have at least one node?
# Should I return the middle node or just its value?

### P - Plan
# 2. Write out in plain English what you want to do:
# I would use two pointers that move at different speeds through the linked list.
# When the fast pointer reaches the end, the slow pointer will be at the middle.

# 3. Translate each sub-problem into pseudocode:
# Set slow and fast to the head of the list.
# Move slow one step and fast two steps while fast can keep moving.
# Return the value at slow when fast reaches the end.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helped me practice the fast and slow pointer pattern.
# It also showed a simple way to solve a linked list problem without counting every node.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
     slow = slow.next
     fast = fast.next.next

    return slow.value

print(find_middle_element(Node(1, Node(2, Node(3, Node(4, Node(5)))))))

# Problem 4: Where do we Begin?
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Can a loop start anywhere in the linked list?
# Should I return the node where the loop begins or its value?

### P - Plan
# 2. Write out in plain English what you want to do:
# I would use two pointers to detect whether the linked list has a cycle.
# If they meet, I would move one pointer back to the head and advance both one step at a time to find the start of the loop.

# 3. Translate each sub-problem into pseudocode:
# Move slow by one step and fast by two steps until they meet or the list ends.
# If they meet, set one pointer to the head.
# Move both pointers one step at a time until they meet again.
# Return the value of the meeting node.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it showed how to find the start of a cycle in a linked list.
# It was useful practice for understanding how two pointers can solve more complex list problems.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def get_loop_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            ptr1 = head
            ptr2 = slow
            while ptr1 is not ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
				
            return ptr1.value

    return None

# Problem 6: Put it in Reverse
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should I reverse the linked list in place or create a new list?
# What should I return if the list is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# I would walk through the list and reverse each pointer as I go.
# I would keep track of the previous node, the current node, and the next node so I do not lose the rest of the list.

# 3. Translate each sub-problem into pseudocode:
# Start with previous as None and current as the head.
# Save the next node, reverse the current pointer, and move both pointers forward.
# Return the previous node as the new head.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because reversing a linked list is a classic interview question.
# It helped me practice updating pointers carefully without breaking the list.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
