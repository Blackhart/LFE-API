from django.contrib import admin

# Register your models here.
from .models.poco.budget import Budget
from .models.poco.bank_account import BankAccount
from .models.poco.budget_group import BudgetGroup
from .models.poco.budget_category import BudgetCategory

admin.site.register(Budget)
admin.site.register(BankAccount)
admin.site.register(BudgetGroup)
admin.site.register(BudgetCategory)
