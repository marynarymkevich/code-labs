languages = ["JavaScript", "Python", "C++", "Java", "Go", "Rust", "TypeScript", "Kotlin"]

first = languages[0]   
last = languages[-1]  
third = languages[2]
second_to_last = languages[-2]

print("List:", languages)
print("First:", first)
print("Third:", third)
print("Second-to-last:", second_to_last)
print("Last:", last)

slice_1 = languages[0:4]
slice_2 = languages[3:5]
slice_3 = languages[::2]

print(slice_1, slice_2, slice_3)

reversed_languages = languages[::-1]
print(reversed_languages)


languages.append("Swift")
print("After append('Swift'):", languages)

languages.insert(2, "Ruby")
print("After insert(2, 'Ruby'):", languages)

languages.remove("C++")
print("After remove('C++'):", languages)

languages.pop()
print("After pop():", languages)

numbers = [34, 65, 1, 35, 12, 56, 1]

length = len(numbers)
minimum = min(numbers)
maximum = max(numbers)
total_sum = sum(numbers)

print("Numeric List:", numbers)
print("Length:", length)
print("Minimum value:", minimum)
print("Maximum value:", maximum)
print("Sum of elements:", total_sum)


list_a = [4, 12, 13, 85, 0]
list_b = ["JavaScript", "Python", "C++", "Java", "Go"]

list_a.sort()
print("list_a.sort:", list_a)

sorted_list_b_desc = sorted(list_b, reverse=True)
print("sorted list_b:", sorted_list_b_desc)

# sort() is a list method that changes the original list.
# sorted() is a built-in function that creates and returns a new sorted list, leaving the original list unchanged.


list_a = [1, 2, 3, 4]

list_b = list_a
list_b.append(5)

# # Both lists are changed and the same
print("list_a:", list_a)
print("list_b:", list_b)

list_c = list_a.copy()
list_c.pop()
print("list_c without last, list_a is not changed:", list_c, list_a)

#TUPLES

rgb_color = (0, 255, 115)
red, green, blue = rgb_color
print(red, green, blue)


person = ("Maryna", 38, "Stockholm")
name, age, city = person
print(f"My name is {name}! I am {age} years old and live in {city}.")

# tuples are useful when values should not be changed, for example some data remains constant, 
# Also tuples are light and fast


coordinates = [
    (10, 20), 
    (35, 40), 
    (50, 75), 
    (100, 200)
]
print("35, 75: ", coordinates[1][0], coordinates[2][1])


courses_list = ["Python", "Data Structures", "Python", "Web Dev", "Data Structures", "Algorithms"]
courses_set = set(courses_list)

length_list = len(courses_list)
length_set = len(courses_set)

print("courses_list:", courses_list)
print("courses_set:", courses_set)
print(f"Length before: {length_list}")
print(f"Length set: {length_set}")


languages = {"Python", "JavaScript", "C++"}
print("Initial set:", languages)

languages.add("Go")
print("Add 'Go':", languages)

languages.remove("Python")
print("Remove 'Python':", languages)

languages.discard("Java")
print("Discard 'Java' (no change expected):", languages)

print("Python", "Python" in languages)
print("JavaScript", "JavaScript" in languages)

# Set is better because it provides uniqness without additional checks - the code is faster and simplier


## DICTIONARIES
# # Create a dictionary for a laptop
laptop = {
    "brand": "Apple",
    "model": "MacBook Pro",
    "RAM": "16GB",
    "storage": "512GB",
    "price": 1000
}

brand_val = laptop["brand"]
model_val = laptop["model"]
ram_val = laptop["RAM"]
storage_val = laptop["storage"]
price_val = laptop["price"]

print(f"Brand: {brand_val}")
print(f"Model: {model_val}")
print(f"RAM: {ram_val}")
print(f"Storage: {storage_val}")
print(f"Price: ${price_val}")


laptop["price"] = 2000
laptop["operating_system"] = "macOS"
laptop.pop("RAM")

print("Updated Laptop Dictionary:", laptop)

brand = laptop.get("brand")
print("get for existing key:", brand)

weight = laptop.get("weight")
weight_with_default = laptop.get("weight", "1500g")
print("get for not existing key:", weight)
print("get for not existing key with default value:", weight_with_default)

# # when we expect to have the key and want to have programm error if not - use [""]
# # when we don't expect and can use the default value - use get with/without default value

print("Keys:", laptop.keys())
print("Values:", laptop.values())
print("Items:", laptop.items())

course_hours = {
    "AI & Machine Learning": 60,
    "Databases & SQL": 40,
    "Python Programming": 50,
    "Web Development": 45,
    "Data Structures & Algorithms": 55
}

print("Total hours:", sum(course_hours.values()))


## NESTED COLLECTIONS

books = [
    {
        "title": "Pippi Longstocking",
        "author": "Astrid Lindgren",
        "pages": 160,
        "available": True
    },
    {
        "title": "Pancake Pie",
        "author": "Sven Nordqvist", # Pettson and Findus
        "pages": 32,
        "available": False
    },
    {
        "title": "The Gruffalo",
        "author": "Julia Donaldson",
        "pages": 32,
        "available": True
    },
    {
        "title": "Karlsson on the Roof",
        "author": "Astrid Lindgren",
        "pages": 128,
        "available": True
    },
    {
        "title": "Moominland Midwinter",
        "author": "Tove Jansson",
        "pages": 176,
        "available": False
    }
]
print("Title of the third book: ", books[2]["title"])
print("Availability of the last book:", books[-1]["available"])

books[0]["pages"] = 175 
books[1]["language"] = "English"

print("First book (pages changed):", books[0])
print("Second book (new key added):", books[1])


company_departments = {
    "Engineers": ["Aleksei", "Boris", "Sergei"],
    "Testers": ["Olga", "Grigoriy", "Anna"],
    "Design": ["Daria", "Elena"],
    "HR": ["Igor"]
}
print(company_departments)


courses = [
    {
        "name": "Machine Learning",
        "teacher": "John Smith",
        "topics": ["Linear Regression", "Neural Networks", "Deep Learning"]
    },
    {
        "name": "Databases & SQL",
        "teacher": "Ivan Popov",
        "topics": ["Relational Model", "JOINs", "Indexing", "Transactions"]
    },
    {
        "name": "Python Programming",
        "teacher": "Elena Smirnova",
        "topics": ["Data Structures", "Functions", "OOP", "Decorators"]
    }
]
print("Selected topic:", courses[1]["topics"][2])


# Part F

catalogue = [
    {
        "meta": ("ISBN-001", 1945),
        "title": "Pippi Longstocking",
        "type": "Book",
        "genre": "Children",
        "rating": 4.9
    },
    {
        "meta": ("ISBN-002", 1984),
        "title": "Pancake Pie",
        "type": "Book",
        "genre": "Children",
        "rating": 4.8
    },
    {
        "meta": ("GAME-001", 2011),
        "title": "Minecraft",
        "type": "Game",
        "genre": "Sandbox",
        "rating": 4.9
    },
    {
        "meta": ("GAME-002", 2015),
        "title": "The Witcher 3",
        "type": "Game",
        "genre": "RPG",
        "rating": 4.9
    },
    {
        "meta": ("MOVIE-001", 2001),
        "title": "Spirited Away",
        "type": "Movie",
        "genre": "Animation",
        "rating": 4.8
    },
    {
        "meta": ("MOVIE-002", 1999),
        "title": "The Matrix",
        "type": "Movie",
        "genre": "Sci-Fi",
        "rating": 4.7
    },
    {
        "meta": ("ISBN-003", 1999),
        "title": "The Gruffalo",
        "type": "Book",
        "genre": "Children",
        "rating": 4.7
    },
    {
        "meta": ("GAME-003", 2020),
        "title": "Cyberpunk 2077",
        "type": "Game",
        "genre": "RPG",
        "rating": 4.3
    }
]

# without loop
unique_genres = set()

unique_genres.add(catalogue[0]["genre"])
unique_genres.add(catalogue[1]["genre"])
unique_genres.add(catalogue[2]["genre"])
unique_genres.add(catalogue[3]["genre"])
unique_genres.add(catalogue[4]["genre"])
unique_genres.add(catalogue[5]["genre"])
unique_genres.add(catalogue[6]["genre"])
unique_genres.add(catalogue[7]["genre"])

print("Unique genres:", unique_genres)


title_first = catalogue[0]["title"] # 'Pippi Longstocking'
year_second = catalogue[1]["meta"][1] # 1984

catalogue[7]["rating"] = 4.7   # update Cyberpunk rating to 4.7
catalogue[2]["platform"] = "PC"   # add new key 'platform' to Minecraft

has_rpg = "RPG" in unique_genres    # True
has_genre = "genre" in catalogue[0]   # True

catalogue.append({"title": "Dune"})   # add item to catalogue
catalogue.pop()      # remove last item

matrix_type = catalogue[5].get("type", "Unknown")   # 'Movie'
first_keys = list(catalogue[0].keys())       # ['meta', 'title', 'type', 'genre', 'rating']


print("SUMMARY")
print(f"1. [{catalogue[0]['type']}] {catalogue[0]['title']} ({catalogue[0]['meta'][1]}) - Genre: {catalogue[0]['genre']}, Rating: {catalogue[0]['rating']}")
print(f"2. [{catalogue[1]['type']}] {catalogue[1]['title']} ({catalogue[1]['meta'][1]}) - Genre: {catalogue[1]['genre']}, Rating: {catalogue[1]['rating']}")
print(f"3. [{catalogue[2]['type']}] {catalogue[2]['title']} ({catalogue[2]['meta'][1]}) - Genre: {catalogue[2]['genre']}, Rating: {catalogue[2]['rating']}")
print(f"4. [{catalogue[3]['type']}] {catalogue[3]['title']} ({catalogue[3]['meta'][1]}) - Genre: {catalogue[3]['genre']}, Rating: {catalogue[3]['rating']}")
print(f"5. [{catalogue[4]['type']}] {catalogue[4]['title']} ({catalogue[4]['meta'][1]}) - Genre: {catalogue[4]['genre']}, Rating: {catalogue[4]['rating']}")
print(f"6. [{catalogue[5]['type']}] {catalogue[5]['title']} ({catalogue[5]['meta'][1]}) - Genre: {catalogue[5]['genre']}, Rating: {catalogue[5]['rating']}")
print(f"7. [{catalogue[6]['type']}] {catalogue[6]['title']} ({catalogue[6]['meta'][1]}) - Genre: {catalogue[6]['genre']}, Rating: {catalogue[6]['rating']}")
print(f"8. [{catalogue[7]['type']}] {catalogue[7]['title']} ({catalogue[7]['meta'][1]}) - Genre: {catalogue[7]['genre']}, Rating: {catalogue[7]['rating']}")


# Part G

list1 = ["marina", "alex", "elena", "dmitry"]
list2 = ["elena", "dmitry", "olga", "maxim"]

set1 = set(list1)
set2 = set(list2)

duplicates = set1.intersection(set2)   # {'elena', 'dmitry'}
all_unique = set1.union(set2)  # {'marina', 'alex', 'elena', 'dmitry', 'olga', 'maxim'}

print("Duplicates:", duplicates)
print("Unique users:", all_unique)


# 2: Nested collection
course_platform = {
    "courses": [
        {
            "course_id": "PY201",
            "title": "Data Structures in Python",
            "teacher": "Dr. Aris",
            "topics": ["Sets", "Dictionaries", "Tuples"],
            "students": ["marina", "alex", "elena"]
        },
        {
            "course_id": "JS101",
            "title": "Frontend Essentials",
            "teacher": "Prof. Nils",
            "topics": ["DOM", "Events", "Async"],
            "students": ["dmitry", "olga"]
        }
    ]
}


# 3
inventory = {
    "smartphone": 25,
    "tablet": 40,
    "charger": 60,
    "smartwatch": 15,
    "adapter": 35
}

inventory["smartphone"] = 20
inventory["tablet"] = 38

total_units = sum(inventory.values())
print("Total stock units:", total_units)


# 4
"""
List:
* Ordered, mutable, allows duplicate items.
* Best fit: A sequence of high scores in a game where items need to be kept in order and updated.

Tuple:
* Ordered, immutable, allows duplicate items.
* Best fit: Storing screen dimensions (width, height) that should remain constant throughout execution.

Set:
* Unordered collection of unique elements with no duplicates.
* Best fit: Tracking online user IDs

Dictionary:
* Unordered key-value pairs mapping unique keys to values.
* Best fit: Representing a book record (title, author, year) for direct field access by key name.
"""