# Generated by Django 4.2.5 on 2023-10-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0003_alter_slider_description_alter_slider_display_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'اسلایدر', 'verbose_name_plural': 'اسلایدرها'},
        ),
    ]