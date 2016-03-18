# coding=utf-8
from PIL import Image
from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from core.files import upload_to
from core.base_model import CommonPage, Common

__author__ = 'alexy'


class PostSection(CommonPage):
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        app_label = 'blog'
        ordering = ('sort',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:section', args=(self.slug,))

    slug = models.SlugField(
        max_length=100,
        verbose_name=u'url'
    )
    sort = models.PositiveIntegerField(default=1, verbose_name=u'Сортировка')


class Post(CommonPage):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'blog'
        ordering = ('sort',)

    def get_absolute_url(self):
        return reverse('blog:detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        super(Post, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (800, 800)
            "Max width and height 800"
            if width > 800:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    postsection = models.ForeignKey(
        to=PostSection,
        verbose_name=u'Категория',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=u'Изображения',
        upload_to=upload_to,
        blank=True,
        null=True
    )
    video = models.TextField(
        verbose_name=u'HTML код видео',
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name=u'Описание'
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=u'url'
    )
    sort = models.PositiveIntegerField(default=1, verbose_name=u'Сортировка')


class PostComment(Common):
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'blog'
        ordering = ('-created',)

    def __unicode__(self):
        return u'Комментарий %s от %s' % (self.name, self.created)

    post = models.ForeignKey(to=Post, verbose_name=u'Статья', null=True, blank=True)
    name = models.CharField(
        verbose_name=u'Ваше имя',
        max_length=256
    )
    mail = models.EmailField(
        verbose_name=u'Ваш email',
        max_length=100
    )
    text = models.TextField(
        verbose_name=u'Сообщение'
    )
