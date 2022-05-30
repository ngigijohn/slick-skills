from django.forms import ModelForm
from django import forms
from .models import UserProfile


class UserProfileForm(ModelForm):

    email = forms.CharField(
        label='Email Address',
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    firstname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Mark'}))
    lastname = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'William'}))
    institution = forms.CharField(
        label='Institution / Company',
        widget=forms.TextInput(attrs={'placeholder': 'IO University'}))
    major = forms.CharField(
        label='Major/ Field of Study',
        widget=forms.TextInput(attrs={'placeholder': 'BST Electronics'}))
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'placeholder': '+000 123 123 123'}))

    class Meta:
        model = UserProfile
        fields = [
         'profile_pic', 'email', 'username', 'firstname', 'lastname', 'institution', 'major', 'phone_number'
        ]
