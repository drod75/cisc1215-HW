from graphics import *

# a = Point(5, 5)
# print(a)
# b = a
# print(b)
# b = Point(10, 10)
# print(a, b)

class Professor():
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f'Professor Name: {self.name}'

class Course():
    def __init__(self, course_id, course_name, instructor) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

prof = Professor('Alice')
print(prof)

course = Course(1215, 'Programming with Python', prof)
print(course.instructor)

course.instructor.name = 'Bob'
print(prof)

a = 5
b = a
print('\n\n',a,b)
b = 6
print(a,b)