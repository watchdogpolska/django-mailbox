from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MailBoxConfig(AppConfig):
    name = 'django_mailbox'
    verbose_name = _("Mail Box")
