# Generated by Django 3.0.5 on 2020-06-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', max_length=300),
        ),
    ]
