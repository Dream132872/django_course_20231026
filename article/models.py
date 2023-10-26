from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='images/articles', max_length=500, verbose_name='تصویر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    score = models.IntegerField(verbose_name='امتیاز')

    def __str__(self):
        return self.title

    def show_image_box(self):
        return mark_safe(f'<img src="{self.image.url}" width="200" />')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
