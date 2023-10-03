from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Address(models.Model):
    street_address = models.CharField(max_length= 200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length= 100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street_address},{self.city},{self.state} {self.postal_code}"
    
    
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    age = models.IntegerField(default= 10, blank= True)
    email = models.EmailField(null=False, blank=False)
    address = models.ForeignKey(Address ,on_delete=models.SET_NULL,null = True,blank= True)
    amount_limit = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

class FetchBook(models.Model):
    book_id =  models.IntegerField(unique=False, default= 10, blank= False)
    image = models.ImageField(upload_to='images' ,default='default_image.jpg')
    title = models.CharField(max_length=10000, blank=False)
    publication_date =  models.CharField(max_length=100, blank=False)
    text_reviews_count = models.IntegerField(blank=True)
    ratings_count = models.IntegerField(blank=True)
    language_code = models.CharField(max_length=100, blank=False)
    isbn =  models.CharField(max_length=100, blank=False)
    isbn13 = models.CharField(max_length=100, blank=False)
    average_rating = models.FloatField(blank=True)
    authors = models.CharField(max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    amount = models.PositiveIntegerField(null=False, blank=False ,default=False)



class BookPurchase(models.Model):
   member = models.ForeignKey(Member, on_delete=models.CASCADE )
   fetchBook = models.ForeignKey(FetchBook,on_delete=models.CASCADE ,default=True,null=True)
   purchase_date = models.DateTimeField(null=False, blank=False)
   expired_date = models.DateTimeField(null=False, blank=False)



