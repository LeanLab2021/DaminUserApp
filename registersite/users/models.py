from django.db import models


CHOICES = [
    ('Male', '男性'),
    ('Female', '女性'),
    ('Other', 'その他'),
]


class User(models.Model):
    name = models.CharField(max_length=200, blank=False,
                            unique=True, primary_key=True)
    birthday = models.DateField(blank=False)
    gender = models.CharField(
        max_length=10, choices=CHOICES, blank=False, default='Male')
