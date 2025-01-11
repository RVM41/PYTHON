#Build a program to manage a university's course catalog.
# #You want to define a base class Course that has the following properties:
#course_code: a string representing the course code (e.g., "CS101")
#course_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3)
# You also want to define two subclasses CoreCourse and ElectiveCourse,
# which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing
# #whether the course is required for a particular major.
# ElectiveCourse should have an additional property elective_type which is a string representing
# the type of elective (e.g., "general", "technical", "liberal arts").
#____----------------------------------------------------------------------------------------

#Answer
#------
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f'{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)'

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return f'{super().__str__()} - Required for Major: {"Yes" if self.required_for_major else "No"}'

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f'{super().__str__()} - Elective Type: {self.elective_type}'

# example
#----------
# Example usage:
course1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
course2 = ElectiveCourse("ART101", "Introduction to Painting", 2, "liberal arts")

print(course1)
print(course2)
