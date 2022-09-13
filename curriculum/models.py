import email
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

class Contacto(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField()
    title= models.CharField(max_length=100)
    message=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True, blank=True,null=True)

    def __str__(self):
        txt = f'{self.title}, fecha: {self.fecha}'
        return txt