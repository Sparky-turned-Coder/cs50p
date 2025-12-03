# students = ["Harry", "Hermoine", "Draco"]
# houses = ["Gryffindor", "Slytherin"]

# here we didn't use the underscore variable. We actually named a variable because we intend to use it.
# for student in students:
#    print(student)

# i is pulling each element in the list one at a time.
# our other argument in the print function also pulls the index number in the list assigned to that element. We added 1 so it doesn't begin at zero.
# for i in range(len(students)):
#    print(i + 1, students[i])

# dict  = dictionary. allows you to associate one thing with another inside a list.
students = {"Harry": "Gryffindor", "Wren": "Hufflepuff", "Draco": "Slytherin"}

for student in students:
    print(student, students[student], sep=", ")
