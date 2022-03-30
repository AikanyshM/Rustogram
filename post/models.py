from django.db import models
from account.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_posted = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateField()

    def __str__(self):
        return f"Comment {self.user.username} - {self.post.title}"

