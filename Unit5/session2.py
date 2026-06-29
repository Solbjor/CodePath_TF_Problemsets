# Problem 5: Tail to Head
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What is the expected behavior when the linked list is empty or has only one node?
# How should the function handle the case where the tail needs to be moved to the head?
### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a function called tail_to_head that takes the head of a linked list as an argument. The function will
# traverse the linked list to find the tail node, then update the next pointer of the tail to point to the head, and finally 
# return the new head of the list (which is the tail node).
# 3. Translate each sub-problem into pseudocode:
# define tail_to_head(head):
#     if head is None or head.next is None:
#         return head
#     current = head
#     while current.next.next:
#         current = current.next
#     tail = current.next
#     current.next = None
#     tail.next = head
#     return tail

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with linked lists, which appear frequently in coding interviews. It also 
# involves understanding how to manipulate pointers and traverse a singly linked list, which is an important skill for 
# solving problems related to these data structures.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def tail_to_head(head):

    if head is None or head.next is None:
        return head

    current = head

    while current.next.next:
        current = current.next

    tail = current.next
    current.next = None
    tail.next = head

    return tail

daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

print_linked_list(tail_to_head(daisy))

# Problem 9: Create a Doubly Linked List
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How do I define a doubly linked list node in Python?
# What is the expected output when I print the values of the doubly linked list from head to tail and from tail to head?
### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a class called Node that represents a node in a doubly linked list. The class will have three 
# attributes: value, next, and prev. I will then create two instances of the Node class to represent the head and 
# tail of the list, and link them together by setting the next attribute of the head to point to the tail and the prev 
# attribute of the tail to point to the head. Finally, I will print the values of the head and tail nodes along with 
# their connections.
# 3. Translate each sub-problem into pseudocode:
# define class Node:
#     define __init__(self, value, next=None, prev=None):
#         value = value
#         next = next
#         prev = prev
# head = Node("Isabelle")
# tail = Node("K.K. Slider")
# head.next = tail
# tail.prev = head
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with Linked Lists. 
# It also involves understanding how to create and manipulate a doubly linked list, which is a common data structure used in various applications.

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)

# Problem 10: Print Backwards
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How do I traverse a doubly linked list from the tail to the head?
# What is the expected output when I print the values of the doubly linked list in reverse

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a function called print_reverse that takes the tail of a doubly linked list as an argument. The function will
# traverse the list from the tail to the head using the prev attribute of each node, printing the value of each node along the way.
# 3. Translate each sub-problem into pseudocode:
# define print_reverse(tail):
#     current = tail
#     while current:
#         print current value
#         current = previous node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with doubly linked lists, which are a 
# fundamental data structure in computer science. It also involves understanding how to traverse a linked list in reverse order, 
# which is an important skill for solving a myriad of these types of problems.
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    current = tail

    while current:
        print(current.value, end=" ")
        current = current.prev

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")

isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

print_reverse(saharah)