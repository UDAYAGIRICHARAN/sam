
from django.forms import ModelForm
from .models import customer,customer1
from django.forms import TextInput, Select, NumberInput

class customerform(ModelForm):
    class Meta:
        
            model=customer
            fields=['name','address','income','assets','yearsinbussiness']
            widgets={
                'name':TextInput(attrs={'class':'form-control','placeholder':'Enter name or username'}),
                'address':TextInput(attrs={'class':'form-control','placeholder':'Enter address'}),
                'income':NumberInput(attrs={'class':'form-control','placeholder':'Enter income'}),
                'assets':NumberInput(attrs={'class':'form-control','placeholder':'Enter assets'}),
                'yearsinbussiness':NumberInput(attrs={'class':'form-control','placeholder':'Enter yearsinbussiness'}),
            }


class customerform1(ModelForm):
    class Meta:
            
                model=customer1
                fields=['username','password']
                widgets={
                    'username':TextInput(attrs={'class':'form-control','placeholder':'Enter username' }),
                    
                    
                    'password':TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
                }

                
    

