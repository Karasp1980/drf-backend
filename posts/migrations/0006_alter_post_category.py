# Generated by Django 3.2.19 on 2023-06-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('tip', 'Tip'), ('help_needed', 'Help needed'), ('other', 'Other')], max_length=32),
        ),
    ]