# Generated by Django 4.2.5 on 2023-10-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
