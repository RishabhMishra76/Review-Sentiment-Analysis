# Generated by Django 2.0.2 on 2020-10-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20201010_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_text',
            field=models.CharField(max_length=250),
        ),
    ]
