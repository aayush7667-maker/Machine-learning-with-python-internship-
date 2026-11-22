student = {
    "name": "Aayush",
    "age": 18,
    "grade": "A"
}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
print(student["name"])

student.update({"age": 19})
print(student)

student.pop("grade")
print(student)

student.setdefault("city", "Kathmandu")
print(student)