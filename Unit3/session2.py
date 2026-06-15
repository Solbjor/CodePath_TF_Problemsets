### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#  What should I return if the input list is empty?
# Should I modify the original list or return a new list with the minimum elements removed?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to find the minimum element in the list and remove all occurrences of it, 
# then return the modified list. If the list is empty, I will return an empty list.

# 3. Translate each sub-problem into pseudocode:
# if nums is empty:
#     return []
# min_value = find minimum value in nums
# while min_value exists in nums:
#     remove min_value from nums
# return nums

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it teaches me how to find the minimum value in a list and 
# how to remove all occurrences of a specific value from a list. It also shows how to handle edge 
# cases, such as an empty list.

def delete_minimum_elements(nums):
    removed = []
    nums = nums.copy()

    while nums:
        min_value = min(nums)
        nums.remove(min_value)
        removed.append(min_value)

    return removed

nums = [5, 3, 2, 8, 3, 1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What should I return if the input list is empty?
#   Should I consider uppercase and lowercase characters as the same when counting uniqueness?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   I want to create a dictionary to count the occurrences of each character in the string. 
# Then I will loop through the string again and check the count of each character in the dictionary

# 3. Translate each sub-problem into pseudocode:
# if strings is empty:
#     return ""
# prefix = strings[0]
# for each string s in strings[1:]:
#     while s does not start with prefix:
#         prefix = prefix[:-1]
#         if prefix is empty:
#             return ""
# return prefix

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it teaches me how to find the longest common prefix among a list of strings,
# which is a common problem in coding interviews. It also shows how to handle edge cases, such as an empty list of 
# strings or no common prefix.

def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What should I return if the input string is empty?
#   Should I consider uppercase and lowercase characters as the same when counting uniqueness?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   I want to create a dictionary to count the occurrences of each character in the string. 
# Then I will loop through the string again and check the count of each character in the dictionary
# 3. Translate each sub-problem into pseudocode:
# if str1 is empty:
#     return 0
# count = 0
# for each character c in str1:
#     if c is the same as the previous character:
#         count++
#     else:
#         count = 1
# return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it teaches me how to count consecutive characters in a string, 
# which is a common problem in coding interviews. It also shows how to handle edge cases, such as an empty string.

def count_consecutive_characters(str1):
    if not str1:
        return 0
    count = 1
    max_count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)