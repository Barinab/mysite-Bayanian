# Generated by Django 4.2.4 on 2023-09-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='Edu_nameUni',
            field=models.CharField(max_length=50),
        ),
    ]
