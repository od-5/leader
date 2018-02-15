# coding=utf-8
from PIL import Image
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from core.files import upload_to

__author__ = 'alexy'


class Review(models.Model):
    sort = models.PositiveIntegerField(default=1, verbose_name=u'Сортировка')
    name = models.CharField(verbose_name=u'ФИО', max_length=256)
    city = models.CharField(verbose_name=u'Города', max_length=256)
    text = models.TextField(verbose_name=u'Текст')
    stands = models.IntegerField(verbose_name=u'Количество стендов')
    income = models.IntegerField(verbose_name=u'Доход')
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    phone = models.CharField(verbose_name=u'Контактный телефон', blank=True, null=True, max_length=20)
    site = models.URLField(verbose_name=u'ссылка на сайт', blank=True, null=True)
    photo = models.ImageField(verbose_name=u'Фотография', upload_to=upload_to)

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
        app_label = 'landing'
        ordering = ('id', )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Review, self).save()
        if self.photo:
            image = Image.open(self.photo)
            (width, height) = image.size
            size = (224, 224)
            "Max width and height 350"
            if width > 224:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.photo.path, "PNG")
