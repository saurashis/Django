from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return (f"{self.name}_")

class Product(models.Model):
    name=models.CharField(max_length=50)
    type=models.ForeignKey(Type,blank=True,on_delete=models.CASCADE,related_name='products')
    description=models.TextField()
    price=models.IntegerField()
    lens=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return(f"{self.name}@{self.price}")

    def get_list_gen(self):
        l=self.lens.split(',')
        for i,j in enumerate(l):
            #print(j)
            sub=j.lstrip("['")
            sub=sub.lstrip(" '")
            sub=sub.rstrip("'")
            sub=sub.rstrip("']")
            l[i]=sub
        return (l)
    
class Rating(models.Model):
    rating=models.IntegerField(blank=False, validators=[MinValueValidator(1),MaxValueValidator(5)])
    comments=models.CharField(max_length=200,blank=False)


    
