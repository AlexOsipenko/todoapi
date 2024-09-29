from django.db import models


class Task(models.Model):
    status_choices = [
        ("in_process", "В процессе"),
        ("completed", "Завершено"),
        ("cancelled", "Отменено"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default="process")

    def __str__(self):
        return self.title
