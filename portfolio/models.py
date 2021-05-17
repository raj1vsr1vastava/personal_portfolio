from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title



