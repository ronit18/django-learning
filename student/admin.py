from django.contrib import admin

from student.models import Department, StudentID, Student, Subject, SubjectMarks

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectMarks)
