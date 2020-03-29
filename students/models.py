from django.db import models



# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=25)
    roll_no = models.IntegerField(max_length=10,default=0)

    rack1 = models.CharField(max_length=3,default=0)
    rack2 = models.CharField(max_length=3,default=0)
    rack3 = models.CharField(max_length=3,default=0)
    rack4 = models.CharField(max_length=3,default=0)
    rack5 = models.CharField(max_length=3,default=0)



    def __str__(self):
        return self.name