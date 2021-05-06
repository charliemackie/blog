from django.db import models

# Create your models here.

class Post(models.Model):

    # Define all the categories that an article could be 

    Data = "Data"
    Business = "Business"
    Eng = "Engineering"
    Random = "Random"

    categories = [
		(Data, 'Data'),
		(Business, 'Business'),
		(Eng, 'Engineering'),
        (Random, 'Random')
	]

    category = models.TextField(choices=categories)
    name = models.TextField()
    time_posted = models.DateField()
    content = models.TextField()
    likes = models.IntegerField(default=0)
    