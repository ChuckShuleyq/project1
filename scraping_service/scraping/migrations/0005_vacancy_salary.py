# Generated by Django 4.1.1 on 2023-01-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(blank=True, max_length=30, verbose_name='Зарплата'),
        ),
    ]