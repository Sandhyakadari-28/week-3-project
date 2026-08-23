file1 = open("week3/file1.txt", "r")
file2 = open("week3/file2.txt", "r")
merged = open("week3/merged.txt", "w")

merged.write(file1.read())
merged.write("\n")
merged.write(file2.read())

file1.close()
file2.close()
merged.close()

print("Files merged successfully!")