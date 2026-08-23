file = open("week3/sample.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()