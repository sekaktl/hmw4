from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    upd_date = models.DateTimeField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
	return self


class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    post = models.ForeignKey(Post)

    def __str__(self):
	return self.text
