from django.apps import AppConfig


class CollabMessagesConfig(AppConfig):
    name = 'collab_messages'

    def ready(self):
        import collab_messages.signals

        # register a custom notification
        from spaces_notifications.utils import register_notification
        from django.utils.translation import ugettext_noop as _
        register_notification(
            'unread_message',
            _("You've got a new message."),
            _("You've got a new message.")
        )
