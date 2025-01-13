
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [70, 65, 72]},
    {"name": "Charlie", "grades": [95, 100, 92]},
    {"name": "David", "grades": [60, 58, 64]}
]

res=[{"name":student["name"],"average":((sum(student['grades']))/3) } for student in students if ((sum(student["grades"]))/3) > 75 ]

print(res)