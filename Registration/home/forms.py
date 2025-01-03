from django import forms
from .models import Student, Grade
from datetime import datetime, date
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:

        model = Student
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'birthDate':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'birthPlace':forms.TextInput(attrs={'class':'form-control'}),
            'nationality':forms.Select(attrs={'class':'form-control'}),

            'town_name':forms.TextInput(attrs={'class':'form-control'}),
            'road_name':forms.TextInput(attrs={'class':'form-control'}),
            'transport':forms.Select(attrs={'class':'form-control'}),
            'previous_school':forms.TextInput(attrs={'class':'form-control'}),
            'admission_level':forms.Select(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'term':forms.Select(attrs={'class':'form-control'}),

            'mother_name':forms.TextInput(attrs={'class':'form-control'}),
            #'mother_phone':forms.TextInput(attrs={'class':'form-control'}),

            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            #'father_phone':forms.TextInput(attrs={'class':'form-control'}),

            'guardian_name':forms.TextInput(attrs={'class':'form-control'}),
            'reference':forms.TextInput(attrs={'class':'form-control'}),

            'registration_agent':forms.Select(attrs={'class':'form-control'}),
            'city_name':forms.TextInput(attrs={'class':'form-control'}),
        
            #'option_services' : forms.Textarea(attrs={'class':'form-control','placeholder':'Type in a list form'}),

            'optional_services_required_for_your_child' : forms.Textarea(attrs={'class':'form-control'}),
            
            'payment': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method':forms.Select(attrs={'class':'form-control'}),
            'payment_history': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'payment_baba': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),            
        }


        # def __init__(self, *args, **kwargs):
        #     user = kwargs.pop('registration_agent', None)
        #     super().__init__(*args, **kwargs)
        #     if user:
        #         self.fields['registration_agent'].initial = user


class SignInForm(AuthenticationForm):
    #username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    #password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    
    class Meta :
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
       