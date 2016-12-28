from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=False)
    name = models.CharField(max_length=50)
    principle = models.IntegerField(default=2000)
    players = models.ManyToManyField(User, related_name='players')
    creator = models.ForeignKey(User, related_name='creator')
