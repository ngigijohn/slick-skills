"""Django's command-line utility for administrative tasks."""
import os
import django
from faker import Faker
from random import choice
fake = Faker()
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

MAJOR_CHOICES = [
    'BBA Accounting',
    'BBA Finance',
    'BBA Management',
    'BBIT',
    'BST Automotive Technology',
    'BSc Software Engineering',
    'Bachelor of Education',
    'Bachelor of Music',
    'Bachelor of Arts Development Studies',
    'Bachelor of Arts Theology',
    'Bachelor of Science in Medical Laboratory Science',
    'Bachelor of Science in Public Health',
    'Bachelor of Science in Nursing',
    'Bachelor of Science in Agribusiness',
    'Bachelor of Science in Agriculture',
    'Bachelor of Science in Electronics Technology',
    'Bachelor of Science in Automotive Technology',
    'Bachelor of Science in Mathematics',
    'Bachelor of Science in Chemistry',
    'Bachelor of Science in Biology',
    'Bachelor of Science in Foods, Nutrition and Dietetics',
]

def generate_users(number):
    from django.contrib.auth.models import User
    from users.models import UserProfile
    
    for index in range(number):
        first_name, last_name = fake.first_name(), fake.last_name()
        new_user = User.objects.create(
                username=first_name+last_name,
                password='top_secret'
            )
        new_user.save()
        user_profile = UserProfile.objects.get(user=new_user)
        user_profile.firstname = first_name
        user_profile.lastname = last_name
        user_profile.email = first_name.lower()+last_name.lower()+'@example.com'
        user_profile.institution = 'UEA, Baraton'
        user_profile.major = choice(MAJOR_CHOICES)
        user_profile.phone_number = "+254"+ fake.msisdn()
        user_profile.save()

    print("Done generated: ",number," Users")


def generate_posts(number):
    from django.contrib.auth.models import User
    from posts.models import Post

    
    users = User.objects.all()

    for index in range(number):
        new_post = Post.objects.create(
        user = choice(users)
        ,company_name = fake.company()
        ,location = "Kenya, " + fake.city()
        ,industry = choice(INDUSTRY_CHOICES)[0]
        ,products_and_services = 'products_and_services'
        ,website = choice(INDUSTRY_CHOICES)[0]+fake.tld()
        ,contact = choice(INDUSTRY_CHOICES)[0]+'@'+fake.free_email_domain()
        ,job_title = "Internship for " + fake.job()
        ,job_type = choice(JOB_TYPE_CHOICES)[0]
        ,specialization = choice(INDUSTRY_CHOICES)[0]+" degree"
        ,job_description = fake.sentence(nb_words=40, variable_nb_words=True)
        ,education_and_experience = fake.sentence(nb_words=20, variable_nb_words=True)
        ,application_requirements = 'Resume, Cover Letter, ID copy, Recommendation letter'
        ,application_process = fake.sentence(nb_words=10, variable_nb_words=True)
        ,application_deadline = fake.date_this_decade()
            )
        new_post.save()
    print( "Done generated: ",number ," Posts")
    






def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slickskills.settings')
    try:
        from django.core.management import execute_from_command_line
        django.setup()
        

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?")from exc
    generate_users(10)
    generate_posts(100)


if __name__ == '__main__':
    main()


