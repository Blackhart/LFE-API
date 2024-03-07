from django.db import models

class BankAccount(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    
    def __str__(self):
        return f'BankAccount(id={self.id}, name={self.name}, type={self.type})'