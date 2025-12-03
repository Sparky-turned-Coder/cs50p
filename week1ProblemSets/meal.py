import re

#   Doing this in neovim so that we can continue working on our nvim muscle memory and work on code projects.

#   Implement a program that prompts the user for a time and outputs whether it's breakfast time, lunch time,
#   or dinner time. If it's not time for a meal, don't output anything at all. Assume that the user's input will
#   will be formatted in 24-hour time as #:## or ##:##. And assume that each meal's time range is inclusive.
#   For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.

#   Structure your program wherein 'convert' is a function (that can be called by 'main') that converts time, a str in 24-hour format,
#   to the corresponding number of hours as a 'float'. For instance, given a time like "7:30"(i.e. 7 hours and 30 minutes),
#   'convert' should return 7.5(i.e. 7.5 hours)

#   This version we finished includes the added challenge of also allowing the user to input time in an a.m./p.m. format.
##   Here we have also refined the original code to the cleanest, sharpest revision we can.


def convert_24(time):
    hours, minutes = time.split(":")
    hours, minutes = float(hours), float(minutes)
    return hours + minutes / 60


def convert_12(time):
    # Example: "7:30 p.m." > ["7", "30", "p.m."]
    parts = re.split(r"[: ]", time)
    hour = float(parts[0])
    minute = float(parts[1])
    meridiem = parts[2]
    # Convert am/pm time to 24 hour time in order to use the same meal function
    if meridiem == "p.m." and hour != 12:
        hour += 12
    if meridiem == "a.m." and hour == 12:
        hour = 0
    return hour + minute / 60


def meal_for_hour(hour):
    if 7 <= hour <= 8:
        return "breakfast time"
    elif 12 <= hour <= 13:
        return "lunch time"
    elif 18 <= hour <= 19:
        return "dinner time"
    else:
        return None


def main():
    time = input("What time is it? ").lower().strip()
    parts = re.split(r"[: ]", time)

    if len(parts) == 2:
        hour = convert_24(time)
    elif len(parts) == 3:
        hour = convert_12(time)
    else:
        return
    meal = meal_for_hour(hour)
    if meal:
        print(meal)


if __name__ == "__main__":
    main()
