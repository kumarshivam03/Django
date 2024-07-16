python -m venv env
django-admin startproject p 
python manage.py startapp a
python manage.py runserver


templates->models.py->shell work

python manage.py makemigrations
python manage.py migrate



python manage.py shell
from studCourseRegApp.models import student,course
s1=student(usn= '1RN21CS001',name= 'Harish', sem=6)
s2=student(usn= '1RN21CS002',name= 'Kumar', sem=6)
s3=student(usn= '1RN21CS003',name= 'Chetan', sem=6)

studList=[s1,s2,s3,s4,s5,s6] 
for stud in studList:
...	  stud.save()
...
...

c1=course(courseCode='21CS61',courseName='SE',courseCredits=3)
c2=course(courseCode='21CS62',courseName='FSD',courseCredits=3)
c3=course(courseCode='21CS63',courseName='CGV',courseCredits=3)

courseList=[c1,c2,c3,c4,c5]
for course in courseList:
...  course.save()
...
...

view->urls->setting
