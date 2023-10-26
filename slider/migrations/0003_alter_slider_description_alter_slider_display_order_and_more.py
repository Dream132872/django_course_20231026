# Generated by Django 4.2.5 on 2023-10-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_alter_slider_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.CharField(max_length=600, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='display_order',
            field=models.IntegerField(verbose_name='اولویت نمایش'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=1000, verbose_name='آدرس url'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=200, verbose_name='عنوان آدرس url'),
        ),
    ]