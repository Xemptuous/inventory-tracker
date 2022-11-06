# Generated by Django 4.1.3 on 2022-11-05 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0004_rename_category_transaction_item_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='subhost',
        ),
        migrations.AddField(
            model_name='transaction',
            name='subhost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_tracker.subhost'),
        ),
    ]