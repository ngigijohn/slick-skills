
from django.forms import ModelForm
from django import forms
from .models import Post

INDUSTRY_CHOICES = [
    ('Agriculture', 'Accounting'),
    ('Accounting', 'Accounting'),
    ('Business', 'Business'),
    ('Creativity', 'Creativity'),
    ('Construction', 'Construction'),
    ('Design', 'Design'),
    ('Engineering', 'Engineering'),
    ('Finance', 'Finance'),
    ('Food Service', 'Food Service'),
    ('Government', 'Government'),
    ('Healthcare', 'Hospitality'),
    ('Hospitality', 'Hospitality'),
    ('Manufacturing', 'Manufacturing'),
    ('Management', 'Management'),
    ('Marketing', 'Marketing'),
    ('Manufacturing', 'Manufacturing'),
    ('Retail', 'Retail'),
    ('Technology', 'Technology'),
    ('Other', 'Other')
]
JOB_TYPE_CHOICES = [
    ('Internship', 'Internship'),
    ('Part-time', 'Part-time'),
    ('Fulltime', 'Fulltime'),
    ('Contract', 'Contract'),
]


class PostForm(ModelForm):
    application_process = forms.CharField(widget=forms.Textarea)
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Deloitte'}))

    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nairobi'}))

    products_and_services = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Audit, Consulting, Tax'}))

    industry = forms.TypedChoiceField(
        choices=INDUSTRY_CHOICES, coerce=str)
    specialization = forms.CharField(
        label='Attachment Specialization',
        widget=forms.TextInput(attrs={'placeholder': 'Accountant'}))
    contact = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email/ phone number'}))
    application_requirements = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Resume, Cover letter, Insurance, Recommendation letters'}))

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user', 'bookmarks']

        # fields = [
        #     'company_name',
        #     'company_pic',
        #     'location',
        #     'industry',
        #     'specialization',
        #     'products_and_services',
        #     'contact',
        #     'application_requirements',
        #     'application_process',
        #     'application_deadline']
