# Generated by Django 3.2.16 on 2024-05-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='comment',
            field=models.CharField(blank=True, max_length=25, verbose_name='Comment'),
        ),
    ]
