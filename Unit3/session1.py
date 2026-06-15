### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#  What should I return if the input string is empty?
#  Should I consider spaces and punctuation as characters when reversing the string?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to create an empty string called reversed_str, then loop through the 
# input string from the last character to the first, appending each character to 
# reversed_str. Finally, I return reversed_str.

# 3. Translate each sub-problem into pseudocode:
#   reversed_str = ""
#   for i from len(my_str) - 1 down to 0:
#       reversed_str += my_str[i]
#   return reversed_str

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it teaches me how to loop through a string in reverse order, 
# and how to build a new string by concatenating characters. It also shows how to handle edge cases like an empty string.

def reverse_string(my_str):
    reversed_str = ""
    for i in range(len(my_str) - 1, -1, -1):
        reversed_str += my_str[i]
    return reversed_str

my_str = "live"
print(reverse_string(my_str))


### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What should I return if there are no unique characters in the string?
#   Should I consider uppercase and lowercase characters as the same when counting uniqueness?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   I want to create a dictionary to count the occurrences of each character in the string. 
# Then I will loop through the string again and check the count of each character in the dictionary. 
# The first character with a count of 1 is the first unique character, and I will return its index. 
# If I finish the loop without finding a unique character, I will return -1.

# 3. Translate each sub-problem into pseudocode:
#   char_count = {}
#   for char in my_str:
#       if char in char_count:
#           char_count[char] += 1
#       else:
#           char_count[char] = 1
#   for i in range(len(my_str)):
#       if char_count[my_str[i]] == 1:
#           return i
#   return -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it teaches me how to use a dictionary to count occurrences of characters, 
# and how to loop through a string while keeping track of indices. It also shows how to handle the case where 
# there are no unique characters. 


def first_unique_char(my_str):
    char_count = {}
    for char in my_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i in range(len(my_str)):
        if char_count[my_str[i]] == 1:
            return i
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What should I return if the input list is empty?
#   Should I consider the same word appearing multiple times as a conflict, or only if it appears in both dictionaries?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   I want to create an empty dictionary called conflicts. Then I will 
# loop through the first dictionary, and for each key-value pair, I will check if the key 
# exists in the second dictionary and if the value is the same. If both conditions are true, 
# I will add that key-value pair to the conflicts dictionary. Finally, I will return the conflicts dictionary.

# 3. Translate each sub-problem into pseudocode:
#   conflicts = {}
#   for key, value in venue1_schedule.items():
#       if key in venue2_schedule and value == venue2_schedule[key]:
#           conflicts[key] = value
#   return conflicts

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#
# I chose this problem because it shows us how to loop through a dictionary and access both the key and value at the same time. 
# It also allows for checking the existence of a key in another dictionary, which is a common task when

def min_distance(words, word1, word2):
    index1 = -1
    index2 = -1
    min_dist = float('inf')
    for i in range(len(words)):
        if words[i] == word1:
            index1 = i
        elif words[i] == word2:
            index2 = i
        if index1 != -1 and index2 != -1:
            min_dist = min(min_dist, abs(index1 - index2))
    return min_dist

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)