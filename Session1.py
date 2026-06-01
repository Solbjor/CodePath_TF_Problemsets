### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I count all times or only unique times?
# Does the threshold itself count, or only times strictly less than it?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Go through the list of race times one at a time and check if each time is less than the threshold.
# If it is, increment a counter. Return the final count.

# 3. Translate each sub-problem into pseudocode:
# counter = 0
# for each time in race_times:
#     if time < threshold:
#         counter = counter + 1
# RETURN counter

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it is a common type of problem that can be solved with a simple loop and conditional
#  statement. It also allows for practice with counting and comparing values.
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Does every single item quantity need to be even, or just most of them?
# What should I return if the list is empty?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Go through the list of quantities one at a time and check if each one is even.
# If any quantity is odd, return False immediately. If all are even, return True.

# 3. Translate each sub-problem into pseudocode:
# for each quantity in item_quantities:
#     if quantity modulo 2 != 0:
#         RETURN False
# RETURN True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it allows for practice with the modulo operator and handling 
# edge cases like an empty list.
def can_pair(item_quantities):
    for quant in item_quantities:
        if quant % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I return the positions of every "thistle" in the list, or just whether one exists?
# Should the indexes start at 0 or 1?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Go through the list one item at a time and check whether each item is "thistle".
# If it is, save its index in a new list and return that list at the end.

# 3. Translate each sub-problem into pseudocode:
# indexes = []
# for each index, item in items:
#     IF item == "thistle":
#         append index
# RETURN indexes

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it allows for practice with loops, conditionals, and working with list appending.
def locate_thistles(items):
    indexes = []
    for index, item in enumerate(items):
        if item == "thistle":
            indexes.append(index)
    return indexes

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))