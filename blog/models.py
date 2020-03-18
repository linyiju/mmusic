from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    author = models.CharField(_('作者'), max_length=100, unique=True)
    title = models.CharField(_('標題'), max_length=225)
    contnet = models.TextField(verbose_name=_('內文'))
    created_at = models.DateTimeField(_('建立時間'), auto_now_add=True)
    last_modified_at = models.DateTimeField(_('最後修改時間'), auto_now=True)

    class Meta:
        verbose_name = _('文章發布')
        verbose_name_plural = _('文章發布')

    def __str__(self):
        return self.title
