# Problem 2: Croquembouche 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the function return the list, print the list, or do both?
# - What should the function do if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a queue to visit each cream puff level by level from left to right.
# Add each flavor to a list, then print and return the completed list.

# 3. Translate each sub-problem into pseudocode:
# If the design is empty:
#     Return an empty list
# Create an empty flavors list
# Create a queue containing the root
# While the queue is not empty:
#     Remove the first node
#     Add its flavor to flavors
#     If it has a left child, add it to the queue
#     If it has a right child, add it to the queue
# Print and return flavors

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because level-order traversal is useful for understanding how queues work with binary trees.
# It also helped me practice visiting nodes one level at a time instead of using recursion.

from collections import deque

class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)

        index += 1

        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)

        index += 1

    return root

def print_tree(root):
    if not root:
        return "Empty"

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)

def print_design(design):
    if design is None:
        return []

    flavors = []
    queue = deque([design])

    while queue:
        current = queue.popleft()
        flavors.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print(flavors)
    return flavors

croquembouche = Puff(
    "Vanilla",
    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")),
    Puff("Strawberry")
)

print_design(croquembouche)


# Problem 1: Merging Cookie Orders 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the function modify one of the original trees or create a new tree?
# - What should happen when a node exists in only one of the two trees?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare the nodes in both trees at the same positions.
# Add overlapping values together and use the existing node when only one node is present.

# 3. Translate each sub-problem into pseudocode:
# If order1 is empty:
#     Return order2
# If order2 is empty:
#     Return order1
# Add order2's value to order1's value
# Recursively merge the left children
# Recursively merge the right children
# Return order1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it demonstrates how recursion can combine two tree structures.
# It also helped me practice handling cases where one tree has a node and the other does not.

class TreeNode:
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right


def merge_orders(order1, order2):
    # If one tree has no node here, use the other tree's node
    if order1 is None:
        return order2

    if order2 is None:
        return order1

    # Both nodes overlap, so combine their quantities
    order1.val += order2.val

    # Merge their left and right subtrees
    order1.left = merge_orders(order1.left, order2.left)
    order1.right = merge_orders(order1.right, order2.right)

    return order1

# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]

order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))


# Problem 1 Set 2: Clone Detection 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Do both the node values and the tree structure need to be identical?
# - Are two empty trees considered clones of each other?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare both trees one pair of nodes at a time.
# Return False if their values or structures differ, and recursively compare both subtrees.

# 3. Translate each sub-problem into pseudocode:
# If both nodes are empty:
#     Return True
# If only one node is empty:
#     Return False
# If the node values are different:
#     Return False
# Compare the left subtrees
# Compare the right subtrees
# Return True only if both sides match

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it shows how recursion can compare two binary trees at the same time.
# It also helped me understand that matching values are not enough if the tree structures are different.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_clone(guest1, guest2):
    # Both positions are empty, so they match
    if guest1 is None and guest2 is None:
        return True

    # One position is empty and the other is not
    if guest1 is None or guest2 is None:
        return False

    # The current guests have different values
    if guest1.val != guest2.val:
        return False

    # Both the left and right subtrees must match
    return (
        is_clone(guest1.left, guest2.left)
        and is_clone(guest1.right, guest2.right)
    )

guest1 = TreeNode(
    "John Doe",
    TreeNode("6 ft"),
    TreeNode("Brown Eyes")
)

guest2 = TreeNode(
    "John Doe",
    TreeNode("6 ft"),
    TreeNode("Brown Eyes")
)

guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))
