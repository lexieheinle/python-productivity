from django.db import models

# Create your models here.
class County(models.Model):
  name = models.CharField(max_length=255)
  name_slug = models.SlugField()
  class Meta:
    verbose_name_plural = 'Counties'
  def __unicode__(self):
    return self.name
  def get_absolute_url(self):
    return "/counties/%s/" % self.name_slug
    #return "reports/%s/" % self.name_slug
  
class Lake(models.Model):
  name = models.CharField(max_length=255)
  name_slug = models.SlugField()
  county = models.ForeignKey(County)
  site_id = models.CharField(max_length=3)
  def __unicode__(self):
    return self.name
  
class Report(models.Model):
  lake = models.ForeignKey(Lake)
  date = models.DateField()
  alert = models.BooleanField()
  toxin = models.FloatField()
  ecoli = models.IntegerField()
  def __unicode__(self):
    return "%s on %s" % (self.lake.name, self.date)
  #part 2 django documentation to add lake model to app due by next tuesday