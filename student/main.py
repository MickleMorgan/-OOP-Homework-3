from group import Group
from student import Student


x = Group('IT', 'Extramural', group_size=3)
y = Group('Non_IT', 'full-time', group_size=3)

st1 = Student('1', '1', 'M', 20, 'Ukrainian', 'Attending')
x.add_student(st1)
x.add_student(Student('1', '1', 'M', 20, 'Ukrainian', 'Attending'))
x.add_student(Student('Andriy', 'Kovalenko', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy1', 'Kovalenko1', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy2', 'Kovalenko2', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy3', 'Kovalenko3', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy4', 'Kovalenko4', 'M', 20, 'Ukrainian', 'Attending'))

print(x)