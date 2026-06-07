# Problem 4: Prioritizing Endangered Species Observations
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# How do we organize/sort our list based on heighest to lowest species priority?
# Do we make 2 lists for the priority and non-priority species and combine them after sorting?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to separate the observed species into two groups: priority and non-priority. Then I sort the priority group by their order in priority_species, and sort the non-priority group alphabetically. Finally, I combine them with priority first.

# 3. Translate each sub-problem into pseudocode:
# priority_set = convert priority_species to a set
# priority_list = []
# other_list = []
# for each species in observed_species:
#   if species is in priority_set:
#     add to priority_list
#   else:
#     add to other_list
# sort priority_list by their index in priority_species
# sort other_list alphabetically
# return priority_list + other_list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it teaches me how to organize data based on multiple criteria. Using a set for membership checking is more efficient, and I get to practice sorting with custom keys.

def prioritize_observations(observed_species, priority_species):
    priority_set = set(priority_species)
    priority_list = []
    other_list = []
    
    for species in observed_species:
        if species in priority_set:
            priority_list.append(species)
        else:
            other_list.append(species)
    
    priority_list.sort(key=priority_species.index)
    other_list.sort()
    
    return priority_list + other_list

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Problem 5: Calculating Conservation Statistics
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# What's a distinct average and how do I calculate it from a population list?
# When I remove elements from the list, will it affect my ability to continue the loop?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to find the maximum and minimum values, remove them, calculate their average, and add it to a set. I keep doing this until the list is empty. The set automatically prevents duplicate averages, so I just return its length.

# 3. Translate each sub-problem into pseudocode:
# avgs = empty set
# while species_populations is not empty:
#   maximum = find max value
#   remove maximum from list
#   minimum = find min value
#   remove minimum from list
#   avg = (maximum + minimum) / 2
#   add avg to avgs
# return length of avgs

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it teaches me how to work with sets to track unique values and how to modify a list while iterating through it. It also shows a practical use case for calculating statistics.

def distinct_averages(species_populations):
    maximum = 0
    minimum = 0
    avgs = set()
    avg = 0
    while species_populations:
        maximum = max(species_populations)
        species_populations.remove(maximum)
        minimum = min(species_populations)
        species_populations.remove(minimum)
        avg = (maximum + minimum) / 2
        avgs.add(avg)
    return len(avgs)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

# Problem 7: Count Unique Species
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# How do I check if a character is a digit vs a letter?
# Should "034" and "34" be counted as the same or different species?

### P - Plan
# 2. Write out in plain English what you want to do: 
# I want to go through the ecosystem_data string and replace all letters with spaces, keeping only the numbers. Then I split the cleaned data to get individual numbers and add them to a set. I need to convert them to integers so leading zeros don't create duplicates. Finally, I return the length of the set.

# 3. Translate each sub-problem into pseudocode:
# cleaned_data = ""
# for each character in ecosystem_data:
#   if character is a digit, add it to cleaned_data
#   else, add a space to cleaned_data
# split cleaned_data into a list of strings
# unique_set = empty set
# for each string in the list:
#   convert to integer and add to unique_set
# return length of unique_set

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it teaches me how to clean up data by filtering characters, and how using a set automatically removes duplicates. It also shows why converting to integers matters when dealing with leading zeros.

def count_unique_species(ecosystem_data):
    unique_species = set()
    cleaned_data = ""
    for letter in ecosystem_data:
        if not letter.isdigit():
            cleaned_data += ' '
        else:
            cleaned_data += letter
    
    speciesList = cleaned_data.split()
    for data in speciesList:
        data = int(data)
        unique_species.add(data)
    
    return len(unique_species)

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))