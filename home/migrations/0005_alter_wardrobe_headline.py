# Generated by Django 4.1 on 2022-08-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_wardrobe_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wardrobe',
            name='headline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
