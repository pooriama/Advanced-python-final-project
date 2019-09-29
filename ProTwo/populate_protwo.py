import os
os.environ.setdefault('Django_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


## Fake pop JavaScript
import random
from appTwo.models import User
from faker import Faker

fakegen=Faker()
# topics= ['Search','Social','Marketplace','News','Games']
# def add_topic():
#     t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        # top =add_topic()
        #create the fake data for that entry
        fake_first=fakegen.first_name()
        fake_last=fakegen.last_name()
        fake_email=fakegen.email()
        #create a fake webpage entry
        # webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        userfake=User.objects.get_or_create(firstname=fake_first,lastname=fake_last,email=fake_email)



if __name__=='__main__':
    print("users script!")
    populate(20)
    print ("users fake created successfully")
