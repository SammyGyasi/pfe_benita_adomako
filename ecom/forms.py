from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Product, SupportImage,SubCategory,Services


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']





class ProductForm(forms.ModelForm):
    support_images = forms.ModelMultipleChoiceField(
        queryset=SupportImage.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to True if support images are mandatory
    )

    class Meta:
        model = Product
        fields = ['name', 'product_image', 'price', 'short_description','detailed_description','support_images']


#Sub_category //Sub packages 

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['sub_name', 'sub_product_image1', 'sub_product_image2', 'sub_product_image3', 'detailed_description']

    sub_product_image1 = forms.ImageField()
    sub_product_image2 = forms.ImageField(required=False)
    sub_product_image3 = forms.ImageField(required=False)


#Forms Side

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'service_image', 'description']




#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
