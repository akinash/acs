from django.db import models
from django.utils import timezone

# Create your models here.


class PassEvent(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)

    init_date = models.DateTimeField(
            blank=True, null=True)

    controller = models.TextField(null=True)

    pass_type = models.TextField(null=True)

    card = models.TextField(null=True)

    status = models.TextField(null=True)

    surname = models.TextField(null=True)

    name = models.TextField(null=True)

    patronymic = models.TextField(null=True, blank=True)

    department = models.TextField(null=True)

    def __str__(self):
        return self.name
