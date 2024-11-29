from django.db import models


class StateChoice(models.TextChoices):
    DONE = 'Done', 'Done'
    NOT_DONE = 'Not done', 'Not done'
