# Generated by Django 4.1.3 on 2022-11-05 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0002_alter_subhost_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subhost',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_tracker.host'),
        ),
    ]