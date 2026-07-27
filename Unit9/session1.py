# Problem 2: Croquembouche 

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
# I chose this problem because 
#

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
# I chose this problem because 

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
# 

### P - Plan
# 2. Write out in plain English what you want to do:
# 

# 3. Translate each sub-problem into pseudocode:
# 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because 

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