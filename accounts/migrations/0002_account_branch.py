# Generated by Django 3.2.7 on 2021-10-15 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accounts', to='banks.branch'),
        ),
    ]
