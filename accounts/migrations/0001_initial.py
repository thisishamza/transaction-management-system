# Generated by Django 3.2.7 on 2021-10-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('account_number', models.PositiveIntegerField(unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('address', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
