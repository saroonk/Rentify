
from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    usertype=models.CharField(max_length=200)


class CATEGORY(models.Model):
    Categoryname=models.CharField(max_length=200)


class USERSDETAILS(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to='images/', blank=True, null=True)
    Age=models.IntegerField()
    phone=models.BigIntegerField()
    Address=models.CharField(max_length=300)



class PRODUCT(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Category_name = models.ForeignKey(CATEGORY, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    PRICE_TYPE_CHOICES = [
        ('hour', 'Per Hour'),
        ('day', 'Per Day'),
        ('month', 'Per Month'),
    ]
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE_CHOICES, default='day')
    quantity_available = models.IntegerField()
    is_available = models.BooleanField(default=True)
    posted_time = models.DateTimeField(auto_now_add=True)


class RENTITEM(models.Model):
    product=models.ForeignKey(PRODUCT,on_delete=models.CASCADE)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    status=models.BooleanField(default=False)
    mobile=models.BigIntegerField()
    is_returned = models.BooleanField(default=False)
    return_status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Disapproved", "Disapproved")],
        default="Pending",
    )






    
