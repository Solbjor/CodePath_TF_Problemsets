

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
            opening_tag = stack.pop()
            if tag.strip() == opening_tag.strip():
                continue
            
    return True

html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))