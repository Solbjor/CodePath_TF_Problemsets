# Problem 3: Identify Popular Creators
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What criteria defines a "popular" creator in this context?
# What data structure is used to represent the creators and their popularity?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to loop through the NFT collection and count the number of NFTs created by each creator. Then I 
# want to identify which creators have more than one NFT in the collection and return a list of those creators.

# 3. Translate each sub-problem into pseudocode:
# creator_count = {}
# for nft in nft_collection:
#     creator = nft['creator']
#     if creator in creator_count:
#         creator_count[creator] += 1
#     else:
#         creator_count[creator] = 1
# popular_creators = []
# for creator, count in creator_count.items():
#     if count > 1:
#         popular_creators.append(creator)
# return popular_creators
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# I chose this problem because it helps me practice working with dictionaries to count occurrences,
# and it also involves filtering data based on a condition, which is a common task in programming.


def identify_popular_creators(nft_collection):
    creator_count = {}
    for nft in nft_collection:
        creator = nft['creator']
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1
        
    popular_creators = []
    for creator, count in creator_count.items():
        if count > 1:
            popular_creators.append(creator)

    return popular_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))

# Problem 4: NFT Collection Statistics

def average_nft_value(nft_collection):
    average = 0
    i = 0
    if not nft_collection:
        return 0
    for nft in nft_collection:
        average += nft['value']
        i += 1
    return average / i

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))

# Problem 6: NFT Queue Processing
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# What data structure is the NFT queue represented as?
# What information is contained in each NFT object in the queue?

### P - Plan
# 2. Write out in plain English what you want to do:
# I want to create an empty list to hold the processed NFTs. Then I want to loop through each NFT in the queue,
# simulate the processing time (if needed), and append the name of the NFT to the processed list. Finally, I 
# want to return the list of processed NFTs.

# 3. Translate each sub-problem into pseudocode:
# processed_nfts = []
# for nft in nft_queue:
#     simulate processing time (optional)
#     processed_nfts.append(nft['name'])
# return processed_nfts

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# I chose this problem because it helps me practice working with lists of dictionaries, 
# and it also introduces the concept of simulating processing time, which can be useful in 
# real-world applications where tasks take time to complete.

def process_nft_queue(nft_queue):
    processed_nfts = []
    for nft in nft_queue:
        processed_nfts.append(nft['name'])
    return processed_nfts


nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))

#Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
['Crypto Kitty', 'Galactic Voyage']