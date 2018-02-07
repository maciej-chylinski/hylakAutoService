from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s, %s" %(self.last_name, self.first_name)


class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    #author = models.ForeignKey(Author)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

def offer_item_upload_path(instance, filename):
    return '/'.join(['offer', str(instance.id), filename])

class Offer(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    offer_item_image = models.ImageField(upload_to=offer_item_upload_path, default='/offer/empty_offer_item.jpg')
