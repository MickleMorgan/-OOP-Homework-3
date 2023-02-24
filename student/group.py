from too_much_students import TooMuchStudents
from student_already_exist import StudentAlreadyExist
from student import Student


class Group:
    """
       Class representing a group of students.

       Attributes:
           speciality (str): Name of the group's speciality.
           group_type (str): Type of the group .
           group_size (int): Maximum size limit of the group (default: 10).
           students (list): List of students in the group.
    """

    def __init__(self, speciality, group_type, group_size=10):
        self.speciality = speciality
        self.group_type = group_type
        self.students = []
        self.group_size = group_size

    def add_student(self, student):
        if len(self.students) > self.group_size:
            raise TooMuchStudents(self.group_size)
        if student in self.students:
            raise StudentAlreadyExist(student, self.speciality)
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_student(self, surname):
        find_student = []
        for person in self.students:
            if person.surname == surname:
                find_student.append(person)
        return find_student

    def __str__(self):
        return f'Group:{self.speciality}\n{self.group_type}\n\n' + '\n'.join(map(str, self.students))
