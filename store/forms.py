from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from store.models import Signup

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['fName', 'lName', 'email', 'password1', 'password2', 'number', 'gender', 'user_type']

    fName = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name..'})
    )
    lName = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name..'})
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email..'})
    )
    password1 = forms.CharField(
        label='Password1',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password..'})
    )
    password2 = forms.CharField(
        label='Password2',
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password..'})
    )
    number = forms.CharField(
        label='Number',
        widget=forms.TextInput(attrs={'placeholder': 'Number'})
    )
   
    def clean(self):
        super(User.self).clean()
        number = self.cleaned_data.get('number')
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            self.errors['password'] = self.error_class(
                ['Password must be more than 8 characters']
            )
        if len(number) < 10:
            self.errors['number'] = self.error_class(
                ['Number is not valid, number is less than 10 characters']
            )
        if len(number) > 10:
            self.errors['number'] = self.error_class(
                ['Number is not valid, number is more than 10 characters']
            )    
        return self.cleaned_data