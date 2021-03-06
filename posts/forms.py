
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
    ('Paid Internship', 'Paid Internship'),
]


class PostForm(ModelForm):

    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Deloitte'}))

    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nairobi'}))

    products_and_services = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Audit, Consulting, Tax'}))
    website = forms.URLField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'www.deloitte.com'}))
    industry = forms.TypedChoiceField(
        choices=INDUSTRY_CHOICES, coerce=str)
    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Intern Accountant'}))
    job_type = forms.TypedChoiceField(
        choices=JOB_TYPE_CHOICES, coerce=str)
    specialization = forms.CharField(
        label='Attachment Specialization',
        widget=forms.TextInput(attrs={'placeholder': 'Accounting & Finance'}))
    contact = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email/ phone number'}))
    application_requirements = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Resume, Cover letter, Insurance, Recommendation letters'}))
    application_process = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Submit Required documents via Email/ Website'}))
    education_and_experience = forms.CharField(widget=forms.Textarea)
    job_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user', 'bookmarks']
