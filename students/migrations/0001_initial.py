# Generated by Django 4.1 on 2022-08-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAPIService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('middle_name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('class_name', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
            ],
        ),
    ]