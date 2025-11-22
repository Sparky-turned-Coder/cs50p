# Next lesson, adding colors and printing output on a timer

import time

# Define color codes
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"  # Resets to default terminal color

countdown = 10

if countdown > 0:
    print(red + "Hello, from Red world!")
    time.sleep(0.5)
    print(green + "Hello, from Green World!")
    time.sleep(0.5)
    print(blue + "Hello, from Blue world!")
    time.sleep(0.5)
    countdown == countdown - 1
else:
    print("Let's call it.")
