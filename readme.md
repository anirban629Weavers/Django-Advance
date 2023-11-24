    In case of migrations all the migrations are stored inside the corresponding database like here I'm using the dbsqlite database that means all the migratons are gonna be stored in the database and retrival of migrations are also possible

<hr>

Commands - Django shell

    - python manage.py shell
    - from home.models import *
    - Student(name="Anirban Mishra",age="20",email="a@a.com",address="Kolkata",phone="6294504157")
    - Student.objects.all()


    Suppose for testing purpose you've implemented a function and as you can't run it directly so you must have to run this in shell after importing that file like from [[home.utils import *]] and then run the function

    Using shell insert data
        student_dict={"name":"Rahul","age":"22","phone":"6846984894"}
        Student.objects.create(**student_dict)
