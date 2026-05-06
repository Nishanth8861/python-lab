import matplotlib.pyplot as plt

students = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
