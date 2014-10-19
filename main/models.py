from django.db import models

class Summary(models.Model):
    title = models.TextField(unique=True)
    paragraphs = models.TextField()
    images = models.TextField()
    fetch_date = models.DateTimeField('date', auto_now_add=True)

    def __unicode__(self):
        return self.title
