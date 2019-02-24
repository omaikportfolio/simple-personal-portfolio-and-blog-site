from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    breif = models.TextField()
    description = models.TextField()
    main_image = models.ImageField(upload_to = 'projects',
                                                null = True, blank = True)
    image_two = models.ImageField(upload_to = 'projects',
                                                null = True, blank = True)
    image_three = models.ImageField(upload_to = 'projects',
                                                null = True, blank = True)
    image_four = models.ImageField(upload_to = 'projects',
                                                null = True, blank = True)
    image_five = models.ImageField(upload_to = 'projects',
                                                null = True, blank = True)
    url = models.URLField(null = True, blank = True)
    start_date = models.DateField(null = True, blank = True)
    finish_date = models.DateField(null = True, blank = True)
    review = models.TextField(null = True, blank = True)
    tech = models.ManyToManyField('portfolio.Tech')


    def __str__(self):
        return self.title


class Tech(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
