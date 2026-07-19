# Problem 2: Flower Finding

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should the function return True or False depending on whether the flower is found?
# Can the flowers appear anywhere in the tree, or is the tree ordered?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to search through every node in the tree for a flower whose value
# matches the given name. If I find the flower, I will return True.
# If I search the entire tree without finding it, I will return False.

# 3. Translate each sub-problem into pseudocode:
# If inventory is None:
#     Return False
#
# If inventory.val equals name:
#     Return True
#
# Search for the flower in the left subtree
# Search for the flower in the right subtree
# Return True if it is found in either subtree

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
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


def find_flower(inventory, name):
    if inventory is None:
        return False

    if inventory.val == name:
        return True

    return (
        find_flower(inventory.left, name)
        or find_flower(inventory.right, name)
    )


"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))
print(find_flower(garden, "Sunflower"))

# Problem 4: Adding a New Plant to the Collection

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Is the collection organized as a binary search tree using plant names?
# What should happen if the plant name already exists in the collection?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to add the new plant while preserving the binary search tree order.
# If the new plant's name is alphabetically smaller than the current node's
# value, I will search the left subtree. If it is alphabetically larger,
# I will search the right subtree. When I find an empty position, I will
# create a new node there.

# 3. Translate each sub-problem into pseudocode:
# If collection is None:
#     Return a new TreeNode containing name
#
# If name is less than collection.val:
#     Set collection.left to the result of adding name to the left subtree
#
# Else if name is greater than collection.val:
#     Set collection.right to the result of adding name to the right subtree
#
# Return collection

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)

    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    elif name > collection.val:
        collection.right = add_plant(collection.right, name)

    return collection

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

# Problem 5: Sorting Plants by Rarity

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should the plants be returned from lowest rarity to highest rarity?
# Should the function return the plant names, rarity values, or both?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to traverse the binary search tree in inorder.
# Because the tree is organized by rarity, visiting the left subtree first,
# then the current node, and then the right subtree will return the plants
# from lowest rarity to highest rarity.

# 3. Translate each sub-problem into pseudocode:
# If collection is None:
#     Return an empty list
#
# Recursively sort the plants in the left subtree
# Add the current plant's name to the list
# Recursively sort the plants in the right subtree
# Return the combined list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key        # Plant rarity
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    if collection is None:
        return []

    return (
        sort_plants(collection.left)
        + [collection.val]
        + sort_plants(collection.right)
    )


"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [
    (3, "Monstera"),
    (1, "Pothos"),
    (5, "Witchcraft Orchid"),
    None,
    (2, "Spider Plant"),
    (4, "Hoya Motoskei")
]

collection = build_tree(values)

print(sort_plants(collection))