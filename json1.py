import json
student = {
  "student_name": "John",
  "student_surname": "Paul",
  "age": 24,
  "subject_list": [
    {"subject": "Flexible manufacturing systems", "points": 77.5, "grade": 4.0},
    {"subject": "Basics of data processing", "points": 21.00, "grade": 2.0}
  ]
}

with open("file.json", 'w') as file:
    data = json.dumps(student)
    file.write(data)