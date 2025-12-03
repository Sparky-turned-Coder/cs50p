# Here we have a dictionary for EACH student. They each have 3 keys. Each key has been assigned a value.
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Luna", "house": "Gryffindor", "patronus": "Hare"},
    {"name": "Rowena", "house": "Ravenclaw", "patronus": "Eagle"},
]

# print each value assigned to the 'name' key. Then print the value assigned to 'house' key. And then the 'patronus' key.
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
