# Generated by Django 4.1.5 on 2023-05-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("phone_no", models.BigIntegerField(verbose_name="Phone No.")),
                ("dob", models.DateField(verbose_name="Date of birth")),
                ("address", models.TextField(verbose_name="Address")),
                ("roll_no", models.IntegerField(verbose_name="Roll No.")),
            ],
            options={
                "db_table": "Student_dtl",
            },
        ),
    ]
