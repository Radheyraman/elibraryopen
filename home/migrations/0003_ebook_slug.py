# Generated by Django 3.2.6 on 2021-08-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ebook_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
