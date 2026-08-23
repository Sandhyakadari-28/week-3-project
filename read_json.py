import json

# Read JSON file
with open("week3/student.json", "r") as file:
    data = json.load(file)

# Display the data
print("Student Details:")
print("Name:", data["name"])
print("Roll Number:", data["roll_number"])
print("Course:", data["course"])
print("Marks:", data["marks"])