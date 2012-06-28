from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime


__all__ = ['Option']


OPTION_TYPE_CHOICES = (
    (1, 'Integer'),
    (2, 'Char'),
    (3, 'Date (DD.MM.YYYY)'),
)


class Option(models.Model):
    name = models.SlugField(_('name'))
    value = models.CharField(_('value'), blank=True, null=True, max_length=255)
    type = models.PositiveSmallIntegerField(_('data type'), choices=OPTION_TYPE_CHOICES, default=1)
    comment = models.CharField(_('comment'), max_length=75, blank=True, default=u"")

    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')

    def get_value(self):
        if self.value in [None, u"None"]:
            return None
        if self.type == 1:
            return int(self.value)
        elif self.type == 3:
            day = self.value.split(".")
            return datetime.date(int(day[2]), int(day[1]), int(day[0]))
        else:
            return self.value

    def set_value(self, val):
        if isinstance(val, int):
            self.value = unicode(val)
            self.type = 1
        elif isinstance(val, datetime.date):
            self.value = val.strftime("%d.%m.%Y")
            self.type = 3
        else:
            self.type = 2
            self.value = unicode(val)
        self.save()
