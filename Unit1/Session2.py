### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I remove all occurrences or just the first one?
# Should the function modify the list in place or return a new list?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Remove all occurrences of the secret identity from the list.

# 3. Translate each sub-problem into pseudocode:
# while secret_identity exists in people:
#     remove the first occurrence

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#

def remove_name(people, secret_identity):
	while secret_identity in people:
		people.remove(secret_identity)
	return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I maintain the relative order of non-zero elements?
# Should the function modify the list in place?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Collect all non-zero elements, then append zeros to the end.

# 3. Translate each sub-problem into pseudocode:
# non_zeros = list of all non-zero elements
# count_zeros = number of zeros
# reconstruct list: non_zeros + [0] * count_zeros

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#

def move_zeroes(lst):
	non_zeros = [x for x in lst if x != 0]
	num_zeros = len(lst) - len(non_zeros)
	lst.clear()
	lst.extend(non_zeros + [0] * num_zeros)
	return lst

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I treat uppercase and lowercase vowels the same?
# Should consonants stay in their original positions?

### P - Plan
# 2. Write out in plain English what you want to do: 
# Extract all vowels, reverse them, then place them back at vowel positions.

# 3. Translate each sub-problem into pseudocode:
# extract vowels from string
# reverse the vowel list
# iterate through string and replace vowels with reversed vowels

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
#

def reverse_vowels(s):
	vowels = "aeiouAEIOU"
	chars = list(s)
	vowel_list = [c for c in chars if c in vowels]
	vowel_list.reverse()
	vowel_index = 0
	for i in range(len(chars)):
		if chars[i] in vowels:
			chars[i] = vowel_list[vowel_index]
			vowel_index += 1
	return ''.join(chars)

s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))