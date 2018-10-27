from django.db import models

class Post(models.Model):

  heading = models.CharField (max_length = 160, null=False)
  body = models.TextField( null=False)
  date = models.DateTimeField()
  user =  models.CharField (max_length = 160)
  img_url = models.URLField()
  slug =  models.SlugField(max_length = 160,unique=True)
  absolute_url = models.CharField(max_length=400, blank=True, editable=False)
  
def __str__(self):
    return self.heading

def get_absolute_url(self ):
     return "/blog/%s" % self.slug

def __unicode__(self):

    return self.heading
