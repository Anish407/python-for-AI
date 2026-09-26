fruits= {"name": "apple", "color": "red", "taste": "sweet"}
list(fruits.keys())  # ['name', 'color', 'taste']
list(fruits.values())  # ['apple', 'red', 'sweet']

items=list(fruits.items())  # [('name', 'apple'), ('color', 'red'), ('taste', 'sweet')]
print(items)  # [('name', 'apple'), ('color', 'red'), ('taste', 'sweet')]
students = [
    {"name": "Anish", "age": 35},
    {"name": "John", "age": 30},
    {"name": "Sara", "age": 28}
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}")