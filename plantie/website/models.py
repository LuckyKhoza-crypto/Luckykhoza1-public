from django.db import models

# Create your models here.
class PostImage(models.Model):
    name = models.CharField('Plant name', max_length=50)
    bio = models.TextField(max_length= 254, blank=True)
    # id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name