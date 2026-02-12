from django import forms
from .models import Employee,Course,Shop

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 
        
#shop form

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        