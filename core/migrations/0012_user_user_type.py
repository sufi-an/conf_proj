# Generated by Django 3.2.6 on 2023-02-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty')], default='Student', max_length=10),
            preserve_default=False,
        ),
    ]