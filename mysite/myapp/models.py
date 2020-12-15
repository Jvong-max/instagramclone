from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    image = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/',
        null=True
    )
    image_description = models.CharField(
        max_length=240,
        null=True
    )

    def __str__(self):
        return self.author.username + " " + self.suggestion
    
    def number_of_likes(self):
        return self.likes.count()

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(SuggestionModel, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment