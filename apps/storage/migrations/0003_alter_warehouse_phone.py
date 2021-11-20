# Generated by Django 3.2.9 on 2021-11-19 19:31

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Введите номер телефона, например, +79999999999', max_length=128, region=None, verbose_name='Телефонный номер склада'),
        ),
    ]
