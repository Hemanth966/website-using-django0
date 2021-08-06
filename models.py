from django.db import models
class info(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)

    email=models.EmailField()
    ph_number=models.TextField()
