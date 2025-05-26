from datetime import datetime

# Generate the current timestamp
timestamp = datetime.now().strftime("%d%m_%H%M%S")

# Create the filename with the desired format
filename = f"Zwalm_{timestamp}.txt"

# Include the filename inside the file content
file_content = f"This file is named: {filename}"

# Write to the file
with open(filename, "w") as file:
    file.write(file_content)

print(f"File '{filename}' has been created with content:\n{file_content}")