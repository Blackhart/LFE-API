# Generated by Django 5.0.2 on 2024-03-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_id_suffix_from_foreign_keys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='budget',
        ),
    ]
