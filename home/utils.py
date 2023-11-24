from .models import *

def get_all_students():
    students=Student.objects.all()
    for student in students:
        print(f'{student.name}-{student.age}')
        