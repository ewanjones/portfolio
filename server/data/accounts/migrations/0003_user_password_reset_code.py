# Generated by Django 3.0.3 on 2020-06-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200524_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_reset_code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
