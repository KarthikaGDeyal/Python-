student={
    "id":"st1",
    "name":"diya",
    "age":23,
    "mobile":7902871374,
    "place":"dubai",
    "course":"python",
    "college":"cec"
}
print(student)
student["skills"]="Django"
print(student)

del student["mobile"]
print(student)
