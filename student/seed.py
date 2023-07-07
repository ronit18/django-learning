from faker import Faker
from .models import Department, StudentID, Student, Subject, SubjectMarks

fake = Faker()
import random


def seedDB(n=100) -> None:
    try:
        for _ in range(n):
            departments_obj = Department.objects.all()
            random_index = random.randint(0, len(departments_obj) - 1)
            student_id = f"STU-{random.randint(100, 9999)}"

            department = departments_obj[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(12, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
            student_obj.save()
    except Exception as e:
        print(e)


def seedMarks():
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject, student=student, marks=random.randint(0, 100)
                )

    except Exception as e:
        print(e)
