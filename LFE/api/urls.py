from django.urls import path

from api.views.budget import BudgetList
from api.views.budget import BudgetUpdate
from api.views.budget import BudgetNameUpdate
from api.views.budget import BankAccountsByBudget
from api.views.budget import BudgetGroupsByBudget
from api.views.budget import TransactionsByBudget
from api.views.bank_account import BankAccountList
from api.views.bank_account import BankAccountUpdate
from api.views.bank_account import BankAccountNameUpdate
from api.views.bank_account import TransactionsByBankAccount
from api.views.budget_group import BudgetGroupList
from api.views.budget_group import BudgetGroupUpdate
from api.views.budget_group import BudgetGroupNameUpdate
from api.views.budget_group import BudgetCategoriesByBudgetGroup
from api.views.budget_category import BudgetCategoryList
from api.views.budget_category import BudgetCategoryUpdate
from api.views.budget_category import BudgetCategoryNameUpdate
from api.views.budget_category import BudgetCategoryGroupIdUpdate
from api.views.transaction import TransactionList
from api.views.transaction import TransactionUpdate
from api.views.report import NetWorthReport

urlpatterns = [
    path('budgets/', BudgetList.as_view()),
    path('budgets/<str:id>', BudgetUpdate.as_view()),
    path('budgets/<str:id>/name', BudgetNameUpdate.as_view()),
    path('budgets/<str:id>/bank-accounts', BankAccountsByBudget.as_view()),
    path('budgets/<str:id>/budget-groups', BudgetGroupsByBudget.as_view()),
    path('budgets/<str:id>/transactions', TransactionsByBudget.as_view()),
    path('bank-accounts/', BankAccountList.as_view()),
    path('bank-accounts/<str:id>', BankAccountUpdate.as_view()),
    path('bank-accounts/<str:id>/name', BankAccountNameUpdate.as_view()),
    path('bank-accounts/<str:id>/transactions', TransactionsByBankAccount.as_view()),
    path('budget-groups/', BudgetGroupList.as_view()),
    path('budget-groups/<str:id>', BudgetGroupUpdate.as_view()),
    path('budget-groups/<str:id>/name', BudgetGroupNameUpdate.as_view()),
    path('budget-groups/<str:id>/budget-categories', BudgetCategoriesByBudgetGroup.as_view()),
    path('budget-categories/', BudgetCategoryList.as_view()),
    path('budget-categories/<str:id>', BudgetCategoryUpdate.as_view()),
    path('budget-categories/<str:id>/name', BudgetCategoryNameUpdate.as_view()),
    path('budget-categories/<str:id>/budget-group-id', BudgetCategoryGroupIdUpdate.as_view()),
    path('transactions/', TransactionList.as_view()),
    path('transactions/<str:id>', TransactionUpdate.as_view()),
    path('reports/net-worth', NetWorthReport.as_view()),
]
