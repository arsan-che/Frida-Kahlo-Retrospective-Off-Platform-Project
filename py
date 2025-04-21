# List of painting titles
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Corresponding list of dates for each painting
dates = [1939, 1933, 1946, 1940]

# Combine paintings and dates into a list of tuples
paintings = list(zip(paintings, dates))

# Print the initial list of paintings with dates
print("Initial paintings with dates:", paintings)
