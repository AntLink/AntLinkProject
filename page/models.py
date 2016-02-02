from word.models import Word
from django.utils.translation import ugettext_lazy as _


class Page(Word):

    class Meta:
        proxy = True
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

