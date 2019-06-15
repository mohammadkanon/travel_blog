from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from ckeditor.fields import RichTextField

# Create your models here.

class CommonInfo(models.Model):
    author_name = models.CharField(max_length=100)
    author_pic = models.ImageField(upload_to='images', null=True, blank=True)
    author_status = models.TextField(null=True, blank=True)
    author_details = models.TextField(null=True, blank=True)
    author_fb_url = models.URLField(null=True, blank=True)
    author_twitter_url = models.URLField(null=True, blank=True)
    author_twitter_url = models.URLField(null=True, blank=True)
    author_youtube_url = models.URLField(null=True, blank=True)
    author_email = models.EmailField(null=True, blank=True)

class BestMoments(models.Model):
    best_pic = models.ImageField(upload_to='best', null=True, blank=True)

class Tour(models.Model):
    tour_title = models.CharField(max_length=200, null=True, blank=True)
    tour_content = RichTextUploadingField(null=True, blank=True)
    tour_content2 = RichTextUploadingField(null=True, blank=True, config_name='special')
    tour_pic = models.ImageField(upload_to='tour', null=True, blank=True)


class Comments(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visitor_comment = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)