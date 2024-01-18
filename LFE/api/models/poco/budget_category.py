from django.db import models

from api.models.poco.budget_group import BudgetGroup

class BudgetCategory(models.Model):
    class Meta:
        verbose_name = 'Budget Category'
        verbose_name_plural = 'Budget Categories'
        
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    budget_group_id = models.ForeignKey(BudgetGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'BudgetCategory(id={self.id}, name={self.name}, budget_group_id={self.budget_group_id})'