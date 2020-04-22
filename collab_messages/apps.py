from django.apps import AppConfig

from django.db.models.signals import post_migrate
from collab_messages.signals import create_notice_types, send_mail_if_recipient_offline


class CollabMessagesConfig(AppConfig):
    name = 'collab_messages'

    def ready(self):
        #import collab_messages.signals

        # register a custom notification
        """
        from spaces_notifications.utils import register_notification
        from django.utils.translation import ugettext_noop as _
        register_notification(
            'unread_message',
            _("You've got a new message."),
            _("You've got a new message.")
        )
        """
        from pinax.messages.signals import message_sent
        message_sent.connect(send_mail_if_recipient_offline, sender=self)
        post_migrate.connect(create_notice_types, sender=self)