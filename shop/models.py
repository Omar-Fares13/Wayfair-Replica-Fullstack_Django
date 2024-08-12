from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    category = models.SlugField()
    describe = models.TextField()
    image = models.ImageField(upload_to='static/imgs/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 

