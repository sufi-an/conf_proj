# Generated by Django 3.2.6 on 2023-02-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230224_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='iub_id',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]