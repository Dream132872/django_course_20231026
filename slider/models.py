from django.db import models


# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=600, verbose_name='توضیحات')
    url = models.URLField(max_length=1000, verbose_name='آدرس url')
    url_title = models.CharField(max_length=200, verbose_name='عنوان آدرس url')
    display_order = models.IntegerField(verbose_name='اولویت نمایش')
    image = models.ImageField(upload_to='images/sliders', max_length=500, verbose_name='تصویر اسلایدر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'
