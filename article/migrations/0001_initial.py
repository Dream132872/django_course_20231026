# Generated by Django 4.2.5 on 2023-10-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('text', models.TextField(verbose_name='متن مقاله')),
                ('image', models.ImageField(max_length=500, upload_to='images/articles', verbose_name='تصویر')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('score', models.IntegerField(verbose_name='امتیاز')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
