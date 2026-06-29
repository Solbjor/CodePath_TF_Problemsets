
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

