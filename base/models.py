from django.db import models

# Create your models here.
class Companies(models.Model):
    c_name = models.CharField(max_length=200)
    c_email = models.EmailField(null=False)
    created=models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return self.c_name
    
class Products(models.Model):
    p_name=models.CharField(max_length=400, null=False)
    p_amount=models.CharField(null=True, max_length=300)
    def __str__(self):
        return self.p_name
    
CHOICES = (
    ("fail", "fail"),
    ("mid", "mid"),
    ("done", "done"),
   
)

class Sales(models.Model):
    company_name = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    state = models.CharField(
        max_length = 50,
        choices = CHOICES,
        default = 'fail'
        )
    def __str__(self):
        return self.state

