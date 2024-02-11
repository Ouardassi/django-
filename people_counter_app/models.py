from django.db import models

class PeopleCount(models.Model):
    
    timestamp = models.DateTimeField(auto_now_add=True)
    total_enter=models.IntegerField()
    count = models.IntegerField()
