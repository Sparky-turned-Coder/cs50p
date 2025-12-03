name = input("What's your name? ")

# if name == "Harry" or name == "Hermoine" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
#
#  match name:
#    case "Harry":
#        print("Gryffindor")
#    case "Hermoine":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
#    case "Draco":
#        print("Slytherin")
#    case _:
#        print("Who?")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco" | "Crabb" | "Goyle":
        print("Slytherin")
    case _:
        print("Don't know who that is.")
