# Generated by Django 3.2.5 on 2021-07-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210706_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
