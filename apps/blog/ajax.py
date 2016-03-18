# coding=utf-8
from annoying.decorators import ajax_request
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from core.models import Setup
from .forms import PostCommentForm
from .models import Post

__author__ = 'alexy'


@ajax_request
def load_more_posts(request):
    try:
        count = int(request.GET.get('count'))
        if request.GET.get('section'):
            section = int(request.GET.get('section'))
            qs = Post.objects.filter(postsection__id=section)
        else:
            qs = Post.objects.all()
        if qs.count() <= count:
            return {
                'end': True
            }
        else:
            next = count + 3
            qs = qs[count:next]
            post_list = []
            for post in qs:
                if post.image:
                    image = post.image.url
                else:
                    image = None
                if post.video:
                    video = post.video
                else:
                    video = ''
                raw_description = strip_tags(post.description).split(' ')
                description = ' '.join(raw_description[:50])
                post_list.append({
                    'title': post.title,
                    'created': str(post.created),
                    'video': video,
                    'image': image,
                    'url': post.get_absolute_url(),
                    'description': description,
                    'comment': post.postcomment_set.count()
                })
            return {
                'post_list': post_list,
                'next': next
            }
    except:
        return {
            'error': True
        }


@ajax_request
def postcomment_add(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            try:
                email = Setup.objects.all().first().email
                if not email:
                    email = 'od-5@yandex.ru'
            except:
                email = 'od-5@yandex.ru'
            mail_theme_msg = u'Лидерфраншиз.рф - оставлен комментарий'
            message = u'Оставлен комментарий на статью: http://лидерфраншиз.рф%s' % comment.post.get_absolute_url()
            send_mail(
                mail_theme_msg,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
            return {
                'comment': True
            }
        else:
            return {
                'error': True
            }
    else:
        return {
            'error': True
        }