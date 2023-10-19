# Generated by Django 4.2.5 on 2023-10-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_postimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='name',
            field=models.CharField(max_length=50, verbose_name='plant name'),
        ),
    ]
