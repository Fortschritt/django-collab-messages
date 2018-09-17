from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from pinax.messages.signals import message_sent

from collab_messages.models import CollabThread
from spaces_notifications.mixins import send_manual_notification


def send_mail_if_recipient_offline(sender, **kwargs):
    """ if the recipient of a new message hasn't been active for a while,
        send an email notification.
    """
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


message_sent.connect(send_mail_if_recipient_offline)