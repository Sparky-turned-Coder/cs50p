# Emoticon here is a 'global' variable. Accessable by all functions below.
emoticon = "v.v"


def main():
    # Here we make 'emoticon' modifiable in our main function. Above, the global is only accessible. So here, we allow the "Modifying of a global state". Inside main(),
    # global variable 'emoticon' can be modified.
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    # Here, phrase is a 'local' variable.
    print(phrase + " " + emoticon)


main()


# For better understanding, look harder at what we did up above.
# We defined a function called 'say()' that will take an input. Our placeholder, or 'local' variable, is (phrase). This local variable will be assigned a string value in our main().
# Next, we write the code that 'say()' will execute when called.
# After this, in our 'main()' function, we CALL the 'say()' function, and we pass it a string 'input' which takes the place of the local variable 'phrase'.
# Thus, when we CALL the function 'say()', we are calling " print(phrase + " " + emoticon) ". 'phrase' becomes the string we assigned it, + "a space" + emoticon.
# What we see printed to the terminal is:  (string input) + " " + emoticon      OR      "Is anyone there? v.v"

# So, inside our main(), we declare our 'global' variable EMOTICON. This allows the global variable to be modified locally. Otherwise, it is only accessible, not modifiable.
# Next, we call our say(), which is the first thing printed to the terminal. Notice, it will print the 'global' variable EMOTICON as it is defined above.
# Next, we re-assign our global variable EMOTICON a new value, which we can do because we've included it within the scope of our main().
# Lastly, we call our say() again, which prints a second line to the terminal. It prints a different string input and the new value we assigned to emoticon.
