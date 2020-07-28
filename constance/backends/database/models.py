from django.db import models
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site

from django.utils.translation import ugettext_lazy as _

try:
    from picklefield import PickledObjectField
except ImportError:
    raise ImproperlyConfigured("Couldn't find the the 3rd party app "
                               "django-picklefield which is required for "
                               "the constance database backend.")


class Constance(models.Model):
    key = models.CharField(max_length=255)
    value = PickledObjectField(null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = ['key', 'site']
        verbose_name = _('constance')
        verbose_name_plural = _('constances')
        db_table = 'constance_config'

    def __str__(self):
        return self.key
