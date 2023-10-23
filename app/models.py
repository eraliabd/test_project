from django.db import models
from django.contrib.auth import get_user_model
from django.utils.functional import cached_property

User = get_user_model()


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_solved = models.PositiveIntegerField()
    ball = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    # new
    @cached_property
    def total_ball_value(self):
        return self.number_of_solved * 2

    def __str__(self):
        return self.user.__str__()
