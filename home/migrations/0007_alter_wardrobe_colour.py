# Generated by Django 4.1 on 2022-08-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_wardrobe_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wardrobe',
            name='colour',
            field=models.CharField(default='blue', max_length=200),
        ),
    ]
