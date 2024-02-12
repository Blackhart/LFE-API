from django.db import models

from api.models.poco.bank_account import BankAccount

class Transaction(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    label = models.CharField(max_length=100)
    amount = models.FloatField()
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Transaction(id={self.id}, date={self.date}, label={self.label}, amount={self.amount}, bank_account={self.bank_account})'