
# Problem 1: Graphing Flights

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

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""

flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["JFK", "ATL"],
    "ATL": ["DFW"]
}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

# Problem 2: There and Back

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

def bidirectional_flights(flights):
    for destination in range(len(flights)):
        for neighbor in flights[destination]:
            if destination not in flights[neighbor]:
                return False

    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

# Problem 3: Finding Direct Flights  

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

def get_direct_flights(flights, source):
    direct_flights = []

    for destination in range(len(flights[source])):
        if flights[source][destination] == 1:
            direct_flights.append(destination)

    return direct_flights


flights = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))