from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class AV_Request(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS = (
        ('Open', 'Open'),
        ('In-progress', 'In-progress'),
        ('closed','Closed'),
    )

    def __str__(self):
        return self.title