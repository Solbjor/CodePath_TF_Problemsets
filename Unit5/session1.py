# Problem 3: Update Catchphrase
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How do I update the catchphrase of a Villager instance?
# What is the expected output when I call the greet_player method after updating the catchphrase?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a method called greet_player that takes a player's name as an argument and returns a greeting message that includes the player's name and the Villager's catchphrase. I will then create an instance of the 
# Villager class, update its catchphrase, and call the greet_player method to see the updated greeting.
# 3. Translate each sub-problem into pseudocode:
#     define greet_player(self, player name):
#         return greeting message with player name and catchphrase
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with classes and methods in Python, which are fundamental 
# concepts in object-oriented programming. It also involves updating instance attributes and understanding how they affect 
# the behavior of methods.
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    def greet_player(self, player_name):
        return f"Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"

print(bones.greet_player("Samia"))

# Problem 4: Group by Personality
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How do I filter a list of Villager instances based on their personality type?
# What is the expected output when I call the of_personality_type function with a list of Villager instances and a specific personality type?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a function called of_personality_type that takes a list of Villager instances and a 
# personality type as arguments. The function will loop through the list of Villager instances, check if each 
# villager's personality matches the specified personality type, and if it does, add the villager's name to a 
# new list. Finally, the function will return the list of matching villager names.
# 3. Translate each sub-problem into pseudocode:
# define of_personality_type(townies, personality_type):
#     matching_townies = []
#     for villager in townies:
#         if villager.personality == personality_type:
#             matching_townies.append(villager.name)
#     return matching_townies

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with lists and filtering data based on 
# specific criteria, which is a common task in programming. It also involves understanding how to access 
# instance attributes of objects in a list.
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

def of_personality_type(townies, personality_type):
    matching_townies = []
    for villager in townies:
        if villager.personality == personality_type:
            matching_townies.append(villager.name)
    return matching_townies

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Problem 8: Telephone
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# How do I determine if a message can be passed from one Villager to another through their neighbors?
# What is the expected output when I call the message_received function with two Villager instances that are not neighbors?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create a function called message_received that takes two Villager instances as arguments: the 
# starting villager and the target villager. The function will loop through the neighbors of the starting villager, 
# checking if each neighbor is the target villager. If it finds the target villager, it will return True. If it reaches 
# a villager that has already been visited or has no neighbor, it will return False, indicating that the message cannot 
# be passed to the target villager.

# 3. Translate each sub-problem into pseudocode:
# define message_received(start_villager, target_villager):
#    current = start_villager
#    visited = set()
#    while current is valid:
#        if current is target_villager:
#            return True
#        if current is in visited:
#            return False
#        add current to visited
#        current = current.neighbor
#   return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it allows us to practice working with object-oriented programming concepts, such as 
# creating classes and instances, as well as understanding how to access instance attributes and relationships 
# between objects. Also, it involves implementing conditional logic to determine the flow of messages between villagers.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
def message_received(start_villager, target_villager):
    current = start_villager
    visited = set()

    while current is not None:
        if current == target_villager:
            return True

        if current in visited:
            return False

        visited.add(current)
        current = current.neighbor

    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))