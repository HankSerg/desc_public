from django.db import models
from django.utils import timezone


class Auto(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Action(models.Model):
    """
    Model representing a auto actions (e.g. buy gasoline, repair).
    Дата события, действие
    """
    name = models.CharField(max_length=200, help_text="Действие")
    auto = models.ForeignKey('Auto', on_delete=models.SET_NULL, null=True)
    # пробег
    # дата записи
    # дата обновления
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
