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
