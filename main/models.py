from django.db import models
from django.contrib.auth.models import User

class Summary(models.Model):
    title = models.TextField()
    paragraphs = models.TextField()
    images = models.TextField()
    user = models.ManyToManyField(User, null=True)
    url = models.TextField(unique=True)
    fetch_date = models.DateTimeField('date', auto_now=True)

    def __unicode__(self):
        return self.title
