# coding=utf-8

__author__ = 'alexy'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'Лидер франшиз',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'label': u'Перейти на сайт', 'icon': 'icon-eye-open', 'url': '/'},
        {'label': u'Пользователи', 'icon': 'icon-user', 'models': ('core.user', 'auth.group',)},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('core.setup',)},
        {'label': u'Заявки', 'icon': 'icon-list-alt', 'models': ('ticket.ticket',)},
        {'label': u'Импорт заявок в CSV', 'icon': 'icon-list-alt', 'url': '/ticket/csv/'},
        {'label': u'Отзывы', 'icon': 'icon-list-alt', 'models': ('landing.review',)},
        {'label': u'Продажи', 'icon': 'icon-user', 'models': ('ticket.sale',)},
        # {'label': u'Блог', 'icon': 'icon-edit', 'models': ('blog.blogsetup', 'blog.postsection', 'blog.post', 'blog.postcomment',)},
        {'label': u'Города', 'icon': 'icon-map-marker', 'models': ('city.city',)},
        # {'label': u'Подписчики', 'icon': 'icon-envelope', 'models': ('sender.sender',)},
    ),
}
