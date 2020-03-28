from django.db import models



# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=25)
    roll_no = models.IntegerField(max_length=10,default=0)

    racks = models.CharField(max_length=20,default=0)



    def __str__(self):
        return self.name