# Problem 3: Ivy Cutting
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What should the function return if the tree is empty?
# Should the right vine include only nodes reached by repeatedly following the right child?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to start at the root and repeatedly move to the right child.
# As I visit each node, I will add its value to a result list.
# Once there are no more right children, I will return the result list.

# 3. Translate each sub-problem into pseudocode:
# If root is None:
#     Return an empty list
#
# Create an empty result list
# Set current equal to root
#
# While current is not None:
#     Add current.val to result
#     Set current equal to current.right
#
# Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    if root is None:
        return []

    result = []
    current = root

    while current is not None:
        result.append(current.val)
        current = current.right

    return result


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3"))
)

"""
      Root
      /
    Node1
    /
  Leaf1
"""
ivy2 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1"))
)

print(right_vine(ivy1))
print(right_vine(ivy2))

# Problem 5: Count the Tree Leaves

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What qualifies as a leaf node?
# What should the function return if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to recursively traverse the tree and count every node that has no left or right child.
# If the current node is empty, I will return 0.
# If the current node is a leaf, I will return 1.
# Otherwise, I will count the leaves in the left and right subtrees and add them together.

# 3. Translate each sub-problem into pseudocode:
# If root is None:
#     Return 0
#
# If root has no left child and no right child:
#     Return 1
#
# Count the leaves in the left subtree
# Count the leaves in the right subtree
# Return the sum of both counts

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3"))
)

"""
      Root
      /
    Node1
    /
  Leaf1
"""

oak2 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1"))
)

print(count_leaves(oak1))
print(count_leaves(oak2))

# Problem : 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#  

### P - Plan
# 2. Write out in plain English what you want to do:
# 

# 3. Translate each sub-problem into pseudocode:
# 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# 

