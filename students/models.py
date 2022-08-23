from django.db import models

# Create your models here.


class StudentAPI(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    middle_name = models.CharField(max_length=500)
    age = models.IntegerField()
    class_name = models.CharField(max_length=500)
    department = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + self.last_name + self.middle_name
