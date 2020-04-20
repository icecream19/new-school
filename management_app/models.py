from django.db import models

LEVEL_CHOICES = (
    ('09', 'Class 9 O level'),
    ('10', 'Class 10 O level'),
    ('11', 'AS level'),
    ('12', 'A2 level'),
)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, primary_key=True)
    teacher_description = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name


class Subject(models.Model):
    level = models.CharField(choices=LEVEL_CHOICES, max_length=2)
    subject_name = models.CharField(max_length=50)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    total_seats = models.IntegerField()
    subject_details = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

    class Meta:
        unique_together = (('level', 'subject_name'),)
        

class StudentRegistration(models.Model):
    student_name = models.CharField(max_length=50)
    student_address = models.TextField()
    student_phone = models.CharField(max_length=11)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.student_name


class Season(models.Model):
    season = models.CharField(max_length=2, primary_key=True)
    subject = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.season
    


