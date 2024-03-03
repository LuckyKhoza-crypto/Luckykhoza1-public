from django.db import models
from django.db import models
from gsheets import mixins
from uuid import uuid4


# Create your models here.
class PostImage(models.Model):
    name = models.CharField('Plant name', max_length=50)
    bio = models.TextField(max_length= 254, blank=True)
    # id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Tree(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = '1d5n18wWbVVhvg1x_1J3UHpJPdzRCcrlK'
    model_id_field = 'guid'

    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)

    Tree_ID = models.CharField(max_length=127)
    Species = models.CharField(max_length=127)
    Common_Name = models.CharField(max_length=127)
    Family = models.CharField(max_length=127)
    Waypoint = models.CharField(max_length=127)

    def __str__(self):
        return f'{self.Tree_ID} {self.Species} {self.Common_Name} {self.Family} {self.Waypoint}'
