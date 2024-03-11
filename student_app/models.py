from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    subject1 = models.ForeignKey(Subject, related_name='subject1_students', on_delete=models.CASCADE)
    subject2 = models.ForeignKey(Subject, related_name='subject2_students', on_delete=models.CASCADE)
    subject3 = models.ForeignKey(Subject, related_name='subject3_students', on_delete=models.CASCADE)
    subject4 = models.ForeignKey(Subject, related_name='subject4_students', on_delete=models.CASCADE)
    subject5 = models.ForeignKey(Subject, related_name='subject5_students', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
