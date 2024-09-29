# Generated by Django 5.1.1 on 2024-09-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("process", "В процессе"),
                    ("completed", "Выполнено"),
                    ("cancelled", "Отменено"),
                ],
                default="process",
                max_length=20,
            ),
        ),
    ]
