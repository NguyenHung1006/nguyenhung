# Generated by Django 3.0.5 on 2020-06-15 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200615_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.Comment'),
            preserve_default=False,
        ),
    ]
