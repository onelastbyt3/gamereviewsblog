# Generated by Django 4.2.4 on 2023-09-08 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.review'),
        ),
    ]
