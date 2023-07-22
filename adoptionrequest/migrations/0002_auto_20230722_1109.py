# Generated by Django 3.2.19 on 2023-07-22 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
        ('adoptionrequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptionrequest',
            name='adoption_owner_profile',
        ),
        migrations.RemoveField(
            model_name='adoptionrequest',
            name='profile',
        ),
        migrations.AddField(
            model_name='adoptionrequest',
            name='adoption',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='adoption', to='adoption.adoption'),
            preserve_default=False,
        ),
    ]