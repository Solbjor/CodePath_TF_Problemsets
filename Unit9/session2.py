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

# Problem 1: Balanced Baked Goods Display

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does every node in the tree need to satisfy the balanced condition?
# - Is an empty tree considered balanced?

### P - Plan
# 2. Write out in plain English what you want to do:
# Recursively calculate the height of each subtree.
# If any node has left and right subtree heights that differ by more than one,
# mark the tree as unbalanced.

# 3. Translate each sub-problem into pseudocode:
# Create a helper function that returns the height of a subtree
# If the current node is empty:
#     Return height 0
# Find the height of the left subtree
# If the left subtree is unbalanced:
#     Return -1
# Find the height of the right subtree
# If the right subtree is unbalanced:
#     Return -1
# If the difference between the heights is greater than 1:
#     Return -1
# Return 1 plus the larger subtree height
# Return whether the helper result is not -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helped me practice using recursion to calculate tree height.
# It also showed me how to detect an invalid condition early without repeatedly checking nodes.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_balanced(display):
    def find_height(node):
        if node is None:
            return 0

        left_height = find_height(node.left)

        if left_height == -1:
            return -1

        right_height = find_height(node.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return find_height(display) != -1


# Example Usage:

"""
      🎂
     /  \
   🥮   🍩
       /  \
     🥖    🧁
"""

baked_goods1 = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"]
display1 = build_tree(baked_goods1)

"""
          🥖
         /  \
       🧁    🧁
       /       \
      🍪       🍪
     /           \
    🥐           🥐
"""

baked_goods2 = [
    "🥖", "🧁", "🧁",
    "🍪", None, None, "🍪",
    "🥐", None, None, "🥐"
]

display2 = build_tree(baked_goods2)

print(is_balanced(display1))
print(is_balanced(display2))

# Problem 2: Sum of Cookies Sold Each Day

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does each level of the tree represent one separate day?
# - What should the function return if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a queue to visit the tree one level at a time.
# Add all node values on the current level and store that total in a result list.

# 3. Translate each sub-problem into pseudocode:
# If the tree is empty:
#     Return an empty list
# Create an empty result list
# Create a queue containing the root
# While the queue is not empty:
#     Save the number of nodes currently in the queue
#     Set the current level sum to 0
#     Repeat once for every node on the current level:
#         Remove a node from the queue
#         Add its value to the level sum
#         Add its left child to the queue if it exists
#         Add its right child to the queue if it exists
#     Add the level sum to the result list
# Return the result list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helped me practice level-order traversal using a queue.
# It also showed me how to process all nodes on the same level as one group.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def sum_each_days_orders(orders):
    if orders is None:
        return []

    result = []
    queue = deque([orders])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            current = queue.popleft()
            level_sum += current.val

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        result.append(level_sum)

    return result


# Example Usage:

"""
      4
     / \
    2   6
   / \
  1   3
"""

order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))

# Problem 3: Sweetness Difference

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the difference be calculated separately for every level?
# - Should a level containing only one node have a difference of zero?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a queue to visit the tree one level at a time.
# For every level, track the smallest and largest sweetness values and add
# their absolute difference to the result list.

# 3. Translate each sub-problem into pseudocode:
# If the tree is empty:
#     Return an empty list
# Create an empty result list
# Create a queue containing the root
# While the queue is not empty:
#     Save the number of nodes on the current level
#     Set the minimum value to positive infinity
#     Set the maximum value to negative infinity
#     Repeat once for each node on the current level:
#         Remove a node from the queue
#         Update the minimum value
#         Update the maximum value
#         Add the left child if it exists
#         Add the right child if it exists
#     Add maximum minus minimum to the result list
# Return the result list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it combines level-order traversal with tracking minimum and maximum values.
# It also helped me practice performing a calculation for each separate tree level.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def sweet_difference(chocolates):
    if chocolates is None:
        return []

    differences = []
    queue = deque([chocolates])

    while queue:
        level_size = len(queue)
        minimum = float("inf")
        maximum = float("-inf")

        for _ in range(level_size):
            current = queue.popleft()

            minimum = min(minimum, current.val)
            maximum = max(maximum, current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        differences.append(abs(maximum - minimum))

    return differences


# Example Usage:

"""
    3
   / \
  9  20
     /  \
    15   7
"""

sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

"""
      1
     / \
    2   3
   / \   \
  4   5   6
"""

sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))
print(sweet_difference(chocolate_box2))
