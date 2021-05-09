from django.db import models

# Create your models here.
GENDER = (("M", "Male"), ("F", "Female"))

GRADE = (("A", "A"), ("B", "B"), ("C", "C"))


class Employee(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    code = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    dob = models.DateTimeField()
    grade = models.CharField(max_length=5,choices=GRADE, null=True, blank=True)

    class Meta:
        abstract = False

    def __str__(self):
        return str(self.name) + " | " + str(self.age) + " | " + str(self.dob) + " | " + str(self.code)


class EmployeeHistoryDetails(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    code = models.IntegerField()

    class Meta:
        abstract = False
        db_table = "employee_history"

    def __str__(self):
        return str(self.name) + " | " + str(self.code)



