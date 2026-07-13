# Problem 2: Top Artists
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should the function detect any cycle in the playlist or only cycles that loop back to a previous song?
# Are we allowed to modify the playlist nodes or must we detect a cycle without altering the list?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use two pointers (slow and fast). Move slow by one and fast by two steps. If they ever meet, a cycle exists. If fast reaches the end, there is no cycle.

# 3. Translate each sub-problem into pseudocode:
# If the head is None, return False.
# Initialize slow and fast to head.
# While fast and fast.next exist:
#   Move slow one step.
#   Move fast two steps.
#   If slow equals fast, return True.
# Return False after the loop.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it demonstrates a common linked-list technique useful for detecting loops efficiently.
# I also chose it because it helps practice using pointers and understanding how to traverse linked lists.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    artist_count = {}
    current = playlist
    while current:
        artist = current.artist
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1
        current = current.next
    return artist_count

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))

# Problem 4: On Repeat
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Should the function detect any cycle in the playlist or only cycles that loop back to a previous song?
# Are we allowed to modify the playlist nodes or must we detect a cycle without altering the list?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use two pointers (slow and fast). Move slow by one and fast by two steps. 
# If they ever meet, a cycle exists. If fast reaches the end, there is no cycle.

# 3. Translate each sub-problem into pseudocode:
# If the head is None, return False.
# Initialize slow and fast to head.
# While fast and fast.next exist:
#   Move slow one step.
#   Move fast two steps.
#   If slow equals fast, return True.
# Return False after the loop.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it demonstrates a common linked-list technique (Floyd's cycle detection) useful for detecting loops efficiently.
# I also chose it because it helps practice using pointers and understanding how to traverse linked lists.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    if not playlist_head:
        return False

    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))

# Problem 6: Volume Control 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What counts as a critical point in the list?
# What should the function return if the list is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk through the linked list, compare each node's value to the next node's value, and count each place where the current value is greater.

# 3. Translate each sub-problem into pseudocode:
# If the list is empty, return 0.
# Set count to 0.
# Start at the head node.
# While the current node has a next node:
#   If current.value > current.next.value, increase count.
#   Move to the next node.
# Return count.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helped me practice linked list traversal and comparisons. 
# I also chose it so students learn how to count specific conditions in a linked list, which is a common task in data processing.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio:
        return 0

    count = 0
    current = song_audio

    while current.next:
        if current.value > current.next.value:
            count += 1
        current = current.next

    return count

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))