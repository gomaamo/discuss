# Generated by Django 3.0.3 on 2020-06-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200609_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
