from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('作者'), on_delete=models.PROTECT, default='')
    title = models.CharField(_('標題'), max_length=225)
    content = models.TextField(verbose_name=_('內文'), null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_('建立時間'), auto_now_add=True)
    last_modified_at = models.DateTimeField(_('最後修改時間'), auto_now=True)

    class Meta:
        verbose_name = _('文章發布')
        verbose_name_plural = _('文章發布')

    def __str__(self):
        return self.title
