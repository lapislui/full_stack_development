import os
import sys
import django
import random

from faker import Faker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'level_two.settings'
django.setup()
from first_app.models import *
fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for _ in range(N):
        # Get a topic for the entry
        top = add_topic()

        # Create fake data for that entry
        fake_name = fakegen.company()
        fake_url = fakegen.url()

        # Create a new entry in the database
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fakegen.date())[0]

if __name__ == '__main__':
    print("Populating the database...Please Wait")
    populate(20)
    print('Populating Complete')