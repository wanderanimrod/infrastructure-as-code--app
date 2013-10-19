from django.db import models


class ListItem(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    
    def __unicode__(self):
        return self.title
