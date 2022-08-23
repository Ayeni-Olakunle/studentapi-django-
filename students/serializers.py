from pyexpat import model
from rest_framework import serializers

from .models import StudentAPI


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAPI
        fields = ["id", "first_name", "last_name",
                  "middle_name", "age", "class_name", "department"]
