# Generated by Django 3.2.8 on 2022-11-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='media')),
            ],
        ),
    ]