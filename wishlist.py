import time

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

# Get an item in a list
print("Suggested gift: {}!".format(books[0]))

# Append to list on the first mark
books.insert(0, "Learning PythonL Powerful Object-Oriented Programming")

# Append an item to end of list
books.append('Learning Python 101 - Graham Morby')

# Append to an item
books[0] += ' - Mark Lutz'

# List all Books
print(books)

# loop over each item
for book in books:
    print("* " + book)

# Get book that starts with P
for book in books:
    if book[0] == 'P':
        print("* " + book)


# Function to display wishlist
def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ':')
    suggested_gift = items.pop(0)
    print("Suggested gift: {}!".format(suggested_gift))
    for item in items:
        print("* " + item)
    print()


# Use the display_wishlist function
display_wishlist('Books', books)
display_wishlist('Video Games', video_games)

# Splitting a string to make a list
quote = "The greatest teacher failure is"
words = quote.split()
for word in words:
    print(word)
    time.sleep(.5)
