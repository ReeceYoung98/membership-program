from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models

GYM_TYPES = (
    ('GYM', 'Gym'),
    ('SWIM', 'Swim'),
    ('SPA', 'Spa')
)


class Membership(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField(max_length=4, choices=GYM_TYPES)
    expiry = models.DateTimeField(default=datetime.now() + timedelta(days=1))
