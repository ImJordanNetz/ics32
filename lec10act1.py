from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'major', 'gpa'])

students = []
students.append(Student("jordan", 18, "CS", 4.0))
students.append(Student("jordan", 18, "CS", 3.5))
students.append(Student("jordan", 18, "CS", 3.0))

s = 0
for student in students:
    s += student.gpa

print(s/3)