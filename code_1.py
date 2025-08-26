# Define input and output 
input_file = 'input.txt'
output_file = 'output.txt'

# Read from the input file
with open(input_file, 'r') as infile:
    content = infile.read()

# Modify the content (convert to uppercase)
modified_content = content.upper()

# Write the modified content to the output file
with open(output_file, 'w') as outfile:
    outfile.write(modified_content)

print(f"Modified content written to '{output_file}'")