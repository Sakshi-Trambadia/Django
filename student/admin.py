from django.contrib import admin
from .models import Student,Product,Review,StudentProfile,Category,Service,Laptop,LaptopSpecification
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Laptop)
admin.site.register(LaptopSpecification)

