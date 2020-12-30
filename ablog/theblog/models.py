from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_like')
    category = models.CharField(max_length=200, default='select category')

    def number_of_likes(self):
        return self.likes.count()


    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
            return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def get_absolute_url(self):
            return reverse('home')
