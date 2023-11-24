from .models import *

def get_all_students():
    students=Student.objects.all()
    for student in students:
        print(f'{student.name}-{student.age}')
        
def get_single_student(name):
    try:
        students=Student.objects.get(name=name)
        print(students.name.capitalize())
    except Exception as e:
        print(e)
    # for student in students: