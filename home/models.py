from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey('Author',null=True,on_delete=models.SET_NULL)
    genre=models.ForeignKey('Genre',null=True,on_delete=models.SET_NULL)
    description=models.TextField(null=True)
    mrp=models.PositiveIntegerField()
    rating=models.FloatField(default=0.0)
    language=models.CharField(max_length=20,null=True)
    edition=models.DateField(null=True)
    pages=models.PositiveIntegerField(null=True)
    publisher=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to='book_image',default='book_image/default.jpg',blank=True,null=True)
    class Meta:
        ordering=('title',)
    def __str__(self):
        return self.title+" by "+self.author.first_name

class Genre(models.Model):
    name=models.CharField(max_length=25)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    class Meta:
        ordering=('first_name','last_name')
    def __str__(self):
        return self.first_name+" "+self.last_name

class BookInstance(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    b_date=models.DateField(null=True)
    active=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    borrower=models.ForeignKey('Profile',related_name='borrowed',null=True,on_delete=models.SET_NULL)
    uploader=models.ForeignKey('Profile',related_name='uploaded',null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.book.title)+" , "+str(self.b_date)
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    balance=models.FloatField(default=0.0)
    address=models.TextField(null=True)
    contact=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rating(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='rating_set')
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])