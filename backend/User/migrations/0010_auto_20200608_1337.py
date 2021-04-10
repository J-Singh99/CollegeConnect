# Generated by Django 3.0.5 on 2020-06-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_sgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='marks_obtained',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sgpa',
            name='sgpa',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
