import pandas as pd

# Load CSV file
data = pd.read_csv("week3/marks.csv")

# Display data
print("Student Data:")
print(data)

# Calculate average marks
print("\nAverage Marks:", data["Marks"].mean())

# Find highest marks
print("Highest Marks:", data["Marks"].max())

# Find lowest marks
print("Lowest Marks:", data["Marks"].min())