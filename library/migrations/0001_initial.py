# Generated by Django 3.2.9 on 2021-11-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=2000, null=True)),
                ('isbn', models.TextField(blank=True, max_length=2000, null=True)),
                ('authors', models.JSONField(blank=True, null=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, max_length=2000, null=True)),
                ('country', models.TextField(blank=True, max_length=2000, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
