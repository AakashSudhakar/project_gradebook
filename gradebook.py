# gradebook.py

class Classroom(object):

    """
    Must be able to display roster for all students as well as GPAs and
    assignment totals, as well as attendances
    """

    def __init__(self, roster, class_name):
        # Initialize roster
        # Initialize class name
        pass

    """
    General assignment manager that accepts input from UI class and sends
    assignment data for sorting
    """
    def add_assign(self):
        pass


class Student(object):

    """
    student must receive a grade (GPA: double) for an assignment (string) and
    must be able to check whether or not student completed the assignment
    """

    def __init__(self):
        #

    """
    If a new student enters the class after the professor's initialization, the
    student's ID will be appended to the end of the name bank and the ID
    """
    student_name_bank = ["Aaron Aaronson", "Adonis Creed", "Barry Benson", "Crazy Cathy", "Doug Dimmadome", "Daryl Dixon", "Ernie Everclear"]
    new_student_counter = 0

    """
    Create subclasses for each individual student ID for students/professors to edit
    """
    student_ids = ["AA001", "AC001", "BB001", "CC001", "DD001", "DD002", "EE001"]

class AA001(Student):


# Perhaps a third class that displays the UI/UX
