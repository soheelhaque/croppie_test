# Generated by Django 3.1.3 on 2020-12-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_croppie', '0004_auto_20201202_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cropped_photo',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
