from django.db import models

class Budget(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Budget(id={self.id}, name={self.name})'