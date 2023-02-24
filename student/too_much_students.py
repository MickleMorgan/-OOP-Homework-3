class TooMuchStudents(Exception):
    """
    Exception raised when trying to add more students than the group size limit.

    Attributes:
        max_group (int): Maximum group size limit.
    """
    def __init__(self, max_group: int):
        self.max_group = max_group

    def __str__(self):
        return f'You can\'t add more than {self.max_group} students'