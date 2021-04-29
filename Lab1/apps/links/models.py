from django.db import models
from django.contrib.auth import models as auth_models


class Link(models.Model):

    name = models.CharField('Link name', max_length=200)
    image = models.ImageField('Image', upload_to='images')
    likes = models.IntegerField('Likes')
    dislikes = models.IntegerField('Dislikes')

    def __str__(self):
        return self.name


class UserLike(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    isLike = models.BooleanField()
