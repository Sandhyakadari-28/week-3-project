import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
marks = [65, 70, 75, 80, 85]

plt.plot(days, marks, marker="o")

plt.title("Marks Progress")
plt.xlabel("Days")
plt.ylabel("Marks")

plt.savefig("week3/line_graph.png")

print("Line graph created successfully!")