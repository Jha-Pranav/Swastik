# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

# import django
# django.setup()

# # Populate with the faker lib

# from apps.first_app.models import Topic,WebPage,AccessRecord
# import random
# from faker import   Faker

# fakegen = Faker()

# TOPICS = ['Social Network','News','Search','Social','Marketplace']

# def add_topic():
#     t = Topic.objects.get_or_create(topic_name=random.choice(TOPICS))[0]
#     t.save()
#     return t

# def populate(N=5):

#     for i in range(N):
#         topic = add_topic()

#         name = fakegen.company()
#         url = fakegen.url()
#         date =fakegen.date()

#         webpage = WebPage.objects.get_or_create(topic=topic,name=name,url=url)[0]

#         AccessRecord.objects.get_or_create(name=webpage,date=date)

# if __name__=="__main__":
#     populate(20)
