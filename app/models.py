from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_solved = models.PositiveIntegerField()
    ball = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
