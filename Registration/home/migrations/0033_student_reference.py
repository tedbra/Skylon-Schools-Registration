# Generated by Django 3.2.25 on 2025-01-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20241204_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reference',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Reference '),
        ),
    ]
