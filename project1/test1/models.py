from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=30, unique=True)
    product_name = models.CharField(max_length=30)
    product_description= models.CharField(max_length=400)
    product_category= models.CharField(max_length=100)
    product_img= models.ImageField(upload_to='images/')
    def __str__(self):
        return self.product_id

class Contact_Querry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_time = models.DateTimeField(("date"), auto_now_add=True)
    
    def __str__(self):
        return self.email
    

