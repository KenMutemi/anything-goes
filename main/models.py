from django.db import models

class Summary(models.Model):
    title = models.TextField()
    paragraphs = models.TextField()
    images = models.TextField()
    url = models.TextField(unique=True)
    fetch_date = models.DateTimeField('date', auto_now=True)

    def __unicode__(self):
        return self.title
