# Problem 3: Ticket Sales
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

def total_sales(ticket_sales):
    total = 0
    for value in ticket_sales.values():
        total += value
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))

# Problem 4: Scheduling Conflict
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
# 

### P - Plan
# 2. Write out in plain English what you want to do: 
# 

# 3. Translate each sub-problem into pseudocode:
# 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# 

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