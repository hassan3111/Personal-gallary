from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # user = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()




class Location(models.Model):
    location_name=models.CharField(max_length=50,blank=False ,null=True)
    

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
    Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.description
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(self):
        image=Photo.objects.get_or_create()
        return image
