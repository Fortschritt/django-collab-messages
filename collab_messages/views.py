from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from pinax.messages.views import InboxView, MessageCreateView, ThreadDeleteView, ThreadView

from .models import CollabThread, CollabMessage
from .util import get_accessible_users

class CollabInboxView(InboxView):

    template_name = "collab_messages/inbox.html"

    def get_context_data(self, **kwargs):
        context = super(CollabInboxView, self).get_context_data(**kwargs)
        context.update({
            "threads": CollabThread.ordered(CollabThread.inbox(self.request.user)),
            "threads_unread": CollabThread.ordered(CollabThread.unread(self.request.user))
        })
        return context


class CollabMessageCreateView(MessageCreateView):

    template_name = "collab_messages/message_create.html"

    def get_success_url(self):
        return CollabMessage.objects.get(pk=self.object.pk).get_absolute_url()

    def form_valid(self, form):
        # check whether the current user is really allowed to contact to_user
        # this is only needed if the user tampered with user ids in the page source
        accessible_users = get_accessible_users(self.request.user)
        if form.cleaned_data['to_user'] in accessible_users:
            print (dir(form.cleaned_data['to_user']))
            return super(CollabMessageCreateView, self).form_valid(form)
        else:
            form.add_error('to_user', _('You can only write to users you share a group with.'))
            return self.form_invalid(form)


class CollabThreadDeleteView(ThreadDeleteView):

    success_url = reverse_lazy("collab_messages:inbox")
    template_name = "collab_messages/thread_confirm_delete.html"


class CollabThreadView(ThreadView):

    model = CollabThread
    template_name = "collab_messages/thread_detail.html"
    success_url = reverse_lazy("collab_messages:inbox")


# for field label translations
ugettext_lazy("To user")
ugettext_lazy("Subject")