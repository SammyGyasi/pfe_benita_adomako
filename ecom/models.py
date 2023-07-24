from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


# models.py
from django.db import models

class SupportImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='support_images')
    image = models.ImageField(upload_to='support_images/')

class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    detailed_description = models.CharField(max_length=2000 ,default='Fill in ')
    short_description = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subcategories')
    sub_name = models.CharField(max_length=40)
    sub_product_image1 = models.ImageField(upload_to='sub_product_image/')
    sub_product_image2 = models.ImageField(upload_to='sub_product_image/', null=True, blank=True)
    sub_product_image3 = models.ImageField(upload_to='sub_product_image/', null=True, blank=True)
    detailed_description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.sub_name} (Product: {self.product.name})"
    

class  Services(models.Model):
    name = models.CharField(max_length=40)
    service_image = models.ImageField(upload_to='service_image/', null=True, blank=True)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Confirmed',' Confirmed'),
        ('Tour Started','Tour Started'),
        ('Tour Ended','Tour Ended'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
