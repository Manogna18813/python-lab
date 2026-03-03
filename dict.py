student = {
   "name": "John",
   "age": 20,
   "grade": "A"
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
removed_value = student.pop("age")
print("Removed Value (age):", removed_value)
print("Dictionary after pop():", student)
del student["grade"]
print("Dictionary after delete:", student)
