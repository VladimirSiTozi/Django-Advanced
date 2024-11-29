from django.contrib.auth import get_user_model
from django.db import models

from toDoApp.todos.choices import StateChoice


UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    assignees = models.ManyToManyField(
        to=UserModel,
        related_name='assigned_todos',
        blank=True,
    )

    state = models.BooleanField(
        choices=[
            (True, StateChoice.DONE),
            (False, StateChoice.NOT_DONE),
        ],
        default=False
    )

    def __str__(self):
        return self.title
