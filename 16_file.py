# File Handling (Reading and Writing)

# Syntax: open("file_path", mode="open_mode")
# Absolute path ex: C:/Users/user/Desktop/file.txt
# Relative path ex: file.txt (relative to the program's current location)

# mode = "r"  # Read mode
# mode = "w"  # Write mode (overwrites the original content)
# mode = "a"  # Append mode (adds new content to the end of the file)

file = open("123.txt", mode="r")  # Open file for reading
print(file.read()) # Read the entire file content (use readline() to read a single line)
file.close()  # Close the file

file = open("123.txt", mode="r")  
for line in file:  # Iterate through the file line by line
    print(line)
file.close()

file = open("123.txt", mode="r")  
print(file.readlines()) # Read all lines and return them as a list of strings
file.close() 

# For writing or appending, simply change "r" to "w" or "a"

# You can also use the 'with' statement (Context Manager)
with open("123.txt", mode="r") as file:  
    print(file.read())
# Using 'with' automatically closes the file, so you don't need to call file.close()