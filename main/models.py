from django.db import models
import ast
from django.contrib.auth.models import User

class Summary(models.Model):
    title = models.TextField()
    paragraphs = models.TextField()
    images = models.TextField()
    user = models.ManyToManyField(User, null=True)
    url = models.TextField(unique=True)
    last_update = models.DateTimeField('date', auto_now=True)

    def get_paragraphs_as_list(self):
        return ast.literal_eval(self.paragraphs)

    def get_images_as_list(self):
        return ast.literal_eval(self.images)

    def __unicode__(self):
        return self.title
