from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    is_verified = models.BooleanField('Is Verified ?', default=False,
                                                        help_text='Indicates if this post is verified or not?'
                                                                'For admin users only')
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
