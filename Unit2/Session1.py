# Problem 3: Ticket Sales
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# What kind of data structure is ticket sales?
# Can we access only the values of a dictionary?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to declare a variable to hold the total. Then I want to loop through
# the values of the dictionary, and add each value to the total. Last I want to
# return the total.

# 3. Translate each sub-problem into pseudocode:
# total = 0
# for value in dictionary.values():
#   add value to total
# return total

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it handles some of the basics of what a dictionary is. There's also a 
# way to solve it with using .values() which is a useful function to know.  

def total_sales(ticket_sales):
    total = 0
    for value in ticket_sales.values():
        total += value
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))


def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, "Artist not found")

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  


# Problem 4: Scheduling Conflict
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Can I access the key and value of a dictionary in a single loop statement?
# How do I check if key-values are the same in both dicitionaries?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to declare a variable to hold the conflicts. Then I want to loop 
# through the first dictionary, and for each key-value pair, check if the 
# key exists in the second dictionary and if the value is the same. 
# If both conditions are true, I want to add that key-value pair to the conflicts variable. 
# Last I want to return the conflicts.

# 3. Translate each sub-problem into pseudocode:
# conflicts = {}
# for key, value in dictionary1.items():
#     if key in dictionary2 and value == dictionary2[key]:
#         add key-value pair to conflicts
# return conflicts

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it shows us how to loop through a dictionary and access both
# the key and value at the same time. It also allows for checking the existence of a key in another dictionary.

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}
    for key, value in venue1_schedule.items():
        if key in venue2_schedule and value == venue2_schedule[key]:
            conflicts[key] = value    
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

# Problem 10: VIP Passes and Guests
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# Should I treat uppercase and lowercase characters as the same VIP pass?
# How do I declare a set in Python and check if a character is in that set?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to first create a set called vip_set, and loop through the characters in 
# vip_passes adding each character to the set. Afterwards I set a count variable = 0, then loop over the
# characters in guests, and if the character is in vip_set, I increment the count, returning the final count.

# 3. Translate each sub-problem into pseudocode:
# vip_set = set()
# for char in list1:
#   vip_set.add(char)
# count = 0
# for char in list2:
#   if char in vip_set:
#       add to count
# return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it introduces sets, which are a new structure people may not be
# familiar. They also have their own set of notation that needs to be used so its good to learn
# how to for instance add or remove from them. 

def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for char in vip_passes:
        vip_set.add(char)
    count = 0
    for char in guests:
        if char in vip_set:
            count += 1
    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))