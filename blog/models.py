from django.db import models
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 50, default = 'Omar M. Abdel-Fatah')
    content = models.TextField()
    date = models.DateTimeField(auto_now = True)
    main_image = models.ImageField(null = True, upload_to ='blog-media')
    ima1 = models.ImageField(null = True, blank = True, upload_to ='blog-media')
    ima2 = models.ImageField(null = True, blank = True, upload_to ='blog-media')

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Articles, related_name = 'comments',
                                                    on_delete = models.CASCADE)
    name = models.CharField(max_length = 50, blank = False, null = False)
    comment = models.TextField(blank = False, null = False)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment
