from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from store.models import Login, User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
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

class CreateLoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']

    email = forms.CharField(
        label='email',
        widget=forms.TextInput(attrs={'placeholder': 'Email..'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password..'})
    )
    