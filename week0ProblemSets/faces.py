# define function called 'convert' that accepts a string input.
# return that same input with :) or :( converted to the corresponding emoji. If neither is given, return input unchanged.


def convert(phrase):
    if phrase.endswith((":)", ":(")):
        print(phrase.replace(":)", "🙂").replace(":(", "🙁"))
    # elif phrase.endswith(":("):
    #    print(phrase.replace(":(", "🙁"))
    else:
        print(phrase)


def main():
    phrase = input(
        "Tell the computer hello or goodbye. It misses you. It likes happy and sad faces. It's very emotional. "
    )
    convert(phrase)


main()
