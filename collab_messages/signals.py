from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_noop as _

def send_mail_if_recipient_offline(sender, **kwargs):
    """ if the recipient of a new message hasn't been active for a while,
        send an email notification.
    """
    # import at this point because of "Apps aren't loaded yet"
    from collab_messages.models import CollabThread
    from spaces_notifications.mixins import send_manual_notification

    sending_user = kwargs["message"].sender
    recipients = kwargs["thread"].users.all()
    recipients = recipients.exclude(pk = sending_user.pk)

    threshold = getattr(settings, "COLLAB_MESSAGES_INACTIVITY_THRESHOLD", 7200) # seconds

    url = CollabThread.objects.get(pk=kwargs["thread"].pk).get_absolute_url()
    for recipient in recipients:
        if (recipient.collab.last_activity +timedelta(seconds=threshold)) < timezone.now():
            send_manual_notification(
                recipient, 
                'unread_message', 
                kwargs["thread"].subject,
                url
            )

def create_notice_types(sender, **kwargs):
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from spaces_notifications.utils import register_notification
        register_notification(
            'unread_message',
            _("You've got a new message."),
            _("You've got a new message.")
        )