# Generated by Django 3.2.8 on 2022-11-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20221118_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]