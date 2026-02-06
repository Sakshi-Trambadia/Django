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
        

class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"    
        
        
        def __str__(self):
         return self.studentId.studentName    

#cat --> #service

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName      
    
    
class Laptop(models.Model):
    laptopId = models.IntegerField()
    brand = models.CharField()
    
    class Meta:
        db_table = "Laptop"
        
    def __str__(self):
        return self.brand
        
class LaptopSpecification(models.Model):
    specId = models.IntegerField()
    laptopId = models.OneToOneField(Laptop,on_delete=models.CASCADE)
    ram = models.IntegerField()
    storage = models.IntegerField()
            
    class Meta:
          db_table = "LaptopSpecification"
        
           



      
        
     
     
