# Problem 2: Breaking the Cycle 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should the function return when there is no cycle?
# Are nodes identified by object identity or by value when detecting a cycle?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use Floyd's cycle-finding algorithm to detect a cycle.
# If a cycle is found, iterate once around the cycle to collect the node values into a list.
# If no cycle is found, return an empty list.

# 3. Translate each sub-problem into pseudocode:
# If head is None, return empty list
# Initialize slow and fast pointers at head
# While fast and fast.next:
#     advance slow by one, fast by two
#     if slow == fast: cycle detected
#         set current = slow
#         do: append current.value; current = current.next until back to slow
#         break and return collected values
# If loop ends with no detection, return empty list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it demonstrates a common linked-list technique (Floyd's cycle detection) 
# useful for detecting loops efficiently. I also chose it because it helps practice using pointers and 
# understanding how to traverse linked lists.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if not evidence:
        return []

    slow = evidence
    fast = evidence
    false_evidence = []

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected, collect false evidence
            current = slow
            while True:
                false_evidence.append(current.value)
                current = current.next
                if current == slow:
                    break
            break

    return false_evidence

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# Problem 3: Prioritizing Suspects 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should the function return if all suspect ratings are below the threshold?
# Should the function maintain the original order of suspects in the output list?

### P - Plan
# 2. Write out in plain English what you want to do:
# Traverse the linked list once, separating nodes into two groups: those with
# ratings less than the threshold and those greater than or equal to it. Maintain
# the original relative order within each group. At the end, link the "less"
# group to the "greater-or-equal" group and return the head of the combined list.

# 3. Translate each sub-problem into pseudocode:
# If the input list is empty return None
# Initialize pointers for the heads and tails of the lesser and greater lists
# Iterate through the original list:
#   If current value < threshold: append to lesser list
#   Else append to greater list
# After iteration, if less list exists, link its tail to the head of greater
# Return the head of less if it exists, otherwise return head of greater

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helps practice linked list manipulation and filtering based on a condition.
# I also chose it because it demonstrates how to maintain the order of elements while partitioning a list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    if not suspect_ratings:
        return None

    less_head = less_tail = None
    greater_head = greater_tail = None

    current = suspect_ratings

    while current:
        if current.value < threshold:
            if not less_head:
                less_head = less_tail = Node(current.value)
            else:
                less_tail.next = Node(current.value)
                less_tail = less_tail.next
        else:
            if not greater_head:
                greater_head = greater_tail = Node(current.value)
            else:
                greater_tail.next = Node(current.value)
                greater_tail = greater_tail.next
        current = current.next

    if less_tail:
        less_tail.next = greater_head
        return less_head
    else:
        return greater_head

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print("Suspect Ratings")
print_linked_list(partition(suspect_ratings, 3))

# Problem 4: Puzzling it Out 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should the function return if one of the timelines is empty?
# Should the merged timeline maintain the order of events from both timelines?

### P - Plan
# 2. Write out in plain English what you want to do:
# Traverse both sorted timelines simultaneously, always taking the smaller
# next event to add to the merged timeline. Continue until both lists are
# exhausted, handling any remaining events from either list.

# 3. Translate each sub-problem into pseudocode:
# If either timeline is empty, return the other timeline
# Create a dummy head and tail pointer for the merged list
# While both timelines have nodes:
#   Compare current events' values
#   Append the smaller event to merged list and advance that timeline
# After the loop, append any remaining nodes from the non-empty timeline
# Return merged list starting at dummy.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helps practice merging two sorted linked lists while maintaining order.
# Also, it demonstrates how to handle edge cases like empty lists and is a common interview question.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_timelines(known_timeline, witness_timeline):
    testNode = Node(0)
    tail = testNode

    while known_timeline and witness_timeline:
        if known_timeline.value < witness_timeline.value:
            tail.next = Node(known_timeline.value)
            known_timeline = known_timeline.next
        else:
            tail.next = Node(witness_timeline.value)
            witness_timeline = witness_timeline.next
        tail = tail.next

    while known_timeline:
        tail.next = Node(known_timeline.value)
        known_timeline = known_timeline.next
        tail = tail.next

    while witness_timeline:
        tail.next = Node(witness_timeline.value)
        witness_timeline = witness_timeline.next
        tail = tail.next

    return testNode.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))
print("Timeline Merge")
print_linked_list(merge_timelines(known_timeline, witness_timeline))