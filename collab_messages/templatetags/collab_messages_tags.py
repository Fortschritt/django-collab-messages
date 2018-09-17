from django import template
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.functions import Lower

from collab_messages.util import get_accessible_users



register = template.Library()




@register.filter
def recipient(thread, user):
    recipient = thread.users.exclude(username=user).first()
    return recipient

@register.filter
def recipient_avatar(thread, user):
    recipient = thread.users.exclude(username=user).first()
    return recipient.profile.avatar


@register.simple_tag
def accessible_users(user):
    return get_accessible_users(user)

@register.inclusion_tag('collab_messages/includes/accessible_users_select.html')
def accessible_users_select(user):
    users = get_accessible_users(user)
    users = users.order_by(Lower('first_name'), 'username')
    return {'accessible_users': users}
    