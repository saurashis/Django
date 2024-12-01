from django.db import models



# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
    lens=models.CharField(max_length=500,blank=True)

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
    
