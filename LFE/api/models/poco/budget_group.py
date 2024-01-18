from django.db import models

from api.models.poco.budget import Budget

class BudgetGroup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'BudgetGroup(id={self.id}, name={self.name}, budget_id={self.budget_id})'