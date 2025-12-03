meow = "meow"

i = 0
while i < 6:
    print(meow)
    i += 1  # this is short for:  i + 1 = i.  It's read from left to right, and then from right to left.

for i in [
    0,
    1,
    2,
]:  # square brackets are indicating a 'list'. Meow is printed for each element in the list, I'm presuming.
    print(meow)


for _ in range(3):  # here we have replaced the variable 'i' with an underscore.
    # This is because we don't need a variable called 'i'. We only need a counter.
    print(meow)

# backslash 'n' gives us bark on new lines. end="" removes print's 'newline' argument
print("bark\n" * 3, end="")


while True:
    n = int(input("What is n? "))
    if n < 0:
        continue
    else:
        break

for i in range(n):
    print("moo")
