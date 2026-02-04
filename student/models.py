from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge= models.IntegerField() #no need to give max length in integer datatype
    studentCity= models.CharField(max_length=40)
    #below field is added after migrating table into db
    #as this field is added later it will give nulll value
    studentEmail=models.CharField(null=True)
    
    
    
    #meta class
    class Meta:
     db_table = "student" #tablename
     
     
class Product(models.Model):
    productName=models.CharField(max_length=100)
    productPrice=models.IntegerField()    
    productDescription=models.TextField()   #no need to give max length
    productStock=models.PositiveIntegerField()
    productColor=models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"
        
class Review(models.Model):
    reviewerName = models.CharField(max_length=100)
    reviewRating = models.PositiveIntegerField()
    reviewComment = models.TextField()
    reviewStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Review"
        
     
     
