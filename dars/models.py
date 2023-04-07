from django.db import models


    
class News1(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=150)
    
class Python(models.Model):
    KursType=models.TextChoices('KursType','Python Java Javascript')
    surname=models.CharField(max_length=30)
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=100)
    year=models.IntegerField()
    kurs=models.CharField(max_length=10,blank=True,choices=KursType.choices)

    
class FTF(models.Model):
    KursType=models.TextChoices('KursType','C++ Java Javascript')
    surname=models.CharField(max_length=30)
    name=models.CharField(max_length=60)
    add_date=models.DateTimeField()
    kurs=models.CharField(max_length=10,blank=True,choices=KursType.choices)
    
class Yangi(models.Model):
    Yangilik=models.TextChoices('Yangilik','Samarqand Toshkent Buxoro')
    surname=models.CharField(max_length=30)
    name=models.CharField(max_length=60)
    add_date=models.DateTimeField()
    Shaharlar=models.CharField(max_length=10,blank=True,choices=Yangilik.choices)
    imgsss=models.ImageField(upload_to='photos/',blank=True,null=True)
    
    
    
    
    def __str__(self):
        return self.surname  + self.name
    

    