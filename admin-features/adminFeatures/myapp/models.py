from django.db import models
from django.core.validators import (
    EmailValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    name_validator = RegexValidator(r"^[A-Za-z]+$", message="only alphabates are allowed")

    first_name = models.CharField(max_length=50, validators= [name_validator])
    last_name = models.CharField(max_length=50, validators= [name_validator])
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid email")]
    )
    date_of_birth = models.DateField()

    def clean(self):
        # date of birth must be past
        if self.date_of_birth >= date.today():
            raise ValidationError({"date_of_birth":"Date must be in the past."})
        
        # date of admission must be after date of birth
        if self.admission_date <= self.date_of_birth:
            raise ValidationError({"admission_date":"admission date must br after DOB"})


    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_date = models.DateField()
    grade = models.CharField(
        max_length=3,
        validators=[RegexValidator(r"^[0-9]+$", "Grede must be numeric")])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.CharField(max_length=3)

    # def __str__(self):
    #     return f"{self.name}-{self.code}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)
    marks = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.student}-{self.course}"
