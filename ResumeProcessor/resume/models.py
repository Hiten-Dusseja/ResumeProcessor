from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255, null=True, blank=True)
 
    def __str__(self) -> str:
        return self.firstname