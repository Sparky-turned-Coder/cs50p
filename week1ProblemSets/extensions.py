# Implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name ends,
# case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf - application/pdf
# .txt - text/plain
# .zip - application/zip

# If the file's name ends with some other suffix or has no suffix at all, output 'application/octet-stream' instead, which is a common default.

# Recall that a 'str' comes with quite a few methods . . .

file = input("Enter the name of your file: ").lower().strip()
file_split = file.split(".")
if file.endswith(".gif"):
    print(f"image/{file_split[-1]}")
elif file.endswith(".png"):
    print(f"image/{file_split[-1]}")
elif file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".jpeg"):
    print(f"image/{file_split[-1]}")
elif file.endswith(".pdf"):
    print(f"application/{file_split[-1]}")
elif file.endswith(".zip"):
    print(f"application/{file_split[-1]}")
elif file.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
