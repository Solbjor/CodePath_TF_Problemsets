# Problem 3: Calculating Total Expenses
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How should I handle cases where the same expense type appears multiple times in the list?
# What should I return if the list of expenses is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a dictionary called expense_summary to store the total amount for each expense type.
# I will loop through the list of expenses, and for each expense, I will check if the expense type is already a key in the dictionary. 
# If it is, I will add the amount to the existing total. If it is not, I will create a new key-value pair in the dictionary with the amount. 
# After processing all expenses, I will find the expense type with the highest total and return both the summary and the most expensive type.

# 3. Translate each sub-problem into pseudocode:
# expense_summary = {}
# for expense in expenses:
#     if expense[0] in expense_summary:
#         add expense[1] to expense_summary[expense[0]]
#     else:
#         set expense_summary[expense[0]] = expense[1]
# maxT = ''
# max = 0
# for expense, value in expense_summary.items():
#     if value greater than max: #
#         maxT = expense
# return (expense_summary, maxT)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it allows us to practice working with dictionaries and handling cases where keys may already exist. 
# It also involves finding the maximum value in a dictionary, which is a common task in data analysis.

def calculate_expenses(expenses):
    expense_summary = {}

    for expense in expenses:
        if expense[0] in expense_summary:
            expense_summary[expense[0]] += expense[1]
        else:
            expense_summary[expense[0]] = expense[1]
    maxT = ''
    max = 0
    for expense, value in expense_summary.items():
        if value > max:
            maxT = expense
    
    return (expense_summary, maxT)

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

# Problem 4: Analyzing word frequency
#### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should I ignore punctuation when analyzing word frequency?
# How should I handle cases where the same word appears in different cases (e.g., "The" vs "the")?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to first convert the entire text to lowercase to ensure that case differences do not affect the word count.
# Then I will split the text into individual words. I will create a dictionary called frequents to store the frequency of each word.
# I will loop through the list of words, and for each word, I will check if it is already a key in the dictionary.
# If it is, I will increment the count. If it is not, I will add it to the dictionary with a count of 1.
# After processing all words, I will return the dictionary containing the word frequencies.

# 3. Translate each sub-problem into pseudocode:
# text = text.lower()
# text = text.split()
# frequents = {}
# for word in text:
#     if word in frequents:
#         frequents[word] += 1
#     else:
#         frequents[word] = 1
# return frequents

# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it allows us to practice working with strings and dictionaries. It also involves text processing,
# which is a common task in many applications such as natural language processing and data analysis.

def word_frequency_analysis(text):
    text = text.lower()
    text = text.split()
    frequents = {}
    for word in text:
        if word in frequents:
            frequents[word] += 1
        else:
            frequents[word] = 1
    return frequents

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))

# Problem 5: Validating HTML Tags
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should I consider self-closing tags (e.g., <br/>) as valid?
# How should I handle cases where there are extra closing tags without corresponding opening tags?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create an empty list called stack to keep track of the opening tags. I will loop through the characters in the HTML string, and whenever I encounter an opening tag, I will push it onto the stack. When I encounter a closing tag, I will check if the stack is empty. If it is,
# I will return False because there is no corresponding opening tag. If the stack is not empty, I will pop the last opening tag from the stack and check if it matches the closing tag. If it does not match, I will return False. After processing all characters, if the stack is empty, I will return True; otherwise, I will return False because there are unmatched opening tags.

# 3. Translate each sub-problem into pseudocode:
# stack = []
# for char in html:
#     if char is an opening tag:
#         push char onto stack
#     elif char is a closing tag:
#         if stack is empty:
#             return False
#         opening_tag = pop from stack
#         if opening_tag does not match char:
#             return False
# if stack is empty:
#     return True
# else:
#     return False

# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it allows us to practice working with stacks, which is a fundamental data structure in computer science. 
# It also involves string manipulation and validation, which are common tasks in web development and programming in general.

def validate_html_tags(html):
    tag = ''
    stacked_tags = []
    stack = []
    for char in html:
        if char == '>':
            tag += char
            stacked_tags.append(tag)
            tag = ''
            continue
        tag += char

    for tag in stacked_tags:
        if '/' not in tag:
            stack.append(tag)
        else:
            if not stack:
                return False
            opening_tag = stack.pop()
            if tag.strip('/<>') != opening_tag.strip('<>/'):
                return False
            
    return True

html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))