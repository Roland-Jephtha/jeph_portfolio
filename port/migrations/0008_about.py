# Generated by Django 3.2.8 on 2022-11-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0007_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]
