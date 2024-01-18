from django.db import models

from api.models.poco.budget import Budget

class BankAccount(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    balance = models.FloatField(default=0)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'BankAccount(id={self.id}, name={self.name}, type={self.type}, balance={self.balance}, budget_id={self.budget_id})'