# Generated by Django 3.0.5 on 2020-06-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200612_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='baiviet',
            name='body',
            field=models.TextField(max_length=1500, null=True),
        ),
    ]
