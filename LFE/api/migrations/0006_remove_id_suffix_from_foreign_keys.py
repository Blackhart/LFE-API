# Generated by Django 5.0.1 on 2024-02-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_add_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='budget_id',
            new_name='budget',
        ),
        migrations.RenameField(
            model_name='budgetcategory',
            old_name='budget_group_id',
            new_name='budget_group',
        ),
        migrations.RenameField(
            model_name='budgetgroup',
            old_name='budget_id',
            new_name='budget',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='bank_account_id',
            new_name='bank_account',
        ),
    ]