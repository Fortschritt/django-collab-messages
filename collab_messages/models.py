from django.core.urlresolvers import reverse
from django.db import models

from pinax.messages.models import Message, Thread

# Create your models here.

class CollabThread(Thread):
    """ Proxy model of the original. We just need to redirect get_absolute_url().
    """

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse("collab_messages:thread_detail", args=[self.pk])


class CollabMessage(Message):
    """ Proxy model of the original. We just need to redirect get_absolute_url().
    """

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return CollabThread.objects.get(pk=self.thread.pk).get_absolute_url()