# List of painting titles
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Corresponding list of dates for each painting
dates = [1939, 1933, 1946, 1940]

# Combine paintings and dates into a list of tuples
paintings = list(zip(paintings, dates))

# Print the initial list of paintings with dates
print("Initial paintings with dates:", paintings)
# New paintings to be added to the list
new_paintings = [('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)]

# Append each new painting to the existing list
for painting in new_paintings:
    paintings.append(painting)

# Print the updated list of paintings with dates
print("Updated paintings with dates:", paintings)

# Calculate the total number of paintings
paintings_length = len(paintings)

# Generate a list of audio tour numbers starting from 1 to the number of paintings
audio_tour_number = list(range(1, paintings_length + 1))

# Combine audio tour numbers with paintings into a master list
master_list = list(zip(audio_tour_number, paintings))

# Print the master list of audio tour numbers with paintings
print("Master list of audio tour numbers with paintings:", master_list)
