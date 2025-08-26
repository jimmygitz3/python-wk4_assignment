# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try opening and reading the file
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
