from faker import Faker
fake = Faker()

print(fake.name())
print(fake.sentence(nb_words=10, variable_nb_words=False))
# 'Lucy Cechtelar'

fake.address()
fake.image(size=(2, 2), hue='purple', luminosity='bright', image_format='png')

import string
import datetime
import os
import sys
import random

# django environment initialization - replace MYAPP w/ your application identifier

if __name__ == "__main__":
    sys.path.append('PATH_TO_APP/')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MYAPP.settings")

from django.contrib.auth.models import User
from MYAPP.models import GameEntry
from MYAPP.models import Profile


def get_random_string(length, stringset=string.ascii_letters):
    return ''.join([stringset[i % len(stringset)] for i in [ord(x) for x in os.urandom(length)]])


def generate_users(n):
    print "Generating %s user(s)..." % n
    print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("#", "username", "firstname", "lastname", "title", "company", "work_email")

    for user_index in xrange(n):
        # create user
        new_user = User.objects.create(
            username=get_random_string(16),
            first_name=get_random_string(16),
            last_name=get_random_string(16),
        )
        new_user.save()

        # create profile for user
        p = Profile.objects.create(user=new_user)
        p.company = get_random_string(16)
        p.title = get_random_string(16)
        p.work_email = "%s@random.com" % get_random_string(5)
        p.save()

        t = "#%s\t%s\t%s\t%s\t%s\t%s\t%s"
        print t % (
            user_index+1,
            new_user.username, new_user.first_name, new_user.last_name,
            p.title, p.company, p.work_email
        )

        # for instance, in a game environment, there can be random entries as well
        for entry_index in xrange(random.randint(1, 100)):
            sys.stdout.write('.')
            sys.stdout.flush()
            g = GameEntry.objects.create(user=new_user)
            g.entry_type = "some_type"
            g.which = "source"
            g.when = datetime.datetime.now()

        print ""


def main(argv):
    if argv.__len__() < 2:
        print "Usage: %s <count>" % argv[0]
        sys.exit(1)
    if not argv[1].isdigit():
        print "Invalid argument: ""%s"" " % argv[1]
        print "Usage: %s <count>" % argv[0]
        sys.exit(1)
    generate_users(int(argv[1]))


if __name__ == "__main__":
    main(sys.argv[0:])