# Generated by Django 3.1.3 on 2020-11-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_croppie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='images/'),
        ),
    ]
