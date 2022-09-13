from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=50)
    text = models.TextField()
    picture = models.ImageField(upload_to='projects/',null=True,blank=True)
    
    def __str__(self):
        txt = f"{self.title}"
        return txt