# Generated by Django 5.0.6 on 2024-05-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_joined_date_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(),
        ),
    ]