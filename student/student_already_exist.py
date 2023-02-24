class StudentAlreadyExist(Exception):
    """
        Exception raised when trying to add a student who is already in the group.

        Attributes:
            student (str): Name of the student.
            group_name (str): Name of the group.
    """
    def __init__(self, student, group_name):
        self.student = student
        self.group_name = group_name

    def __str__(self):
        return f'{self.student} is already in group {self.group_name}'