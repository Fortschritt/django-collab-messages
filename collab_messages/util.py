from django.contrib.auth import get_user_model

from collab_user_views.views import get_accessible_spaces

User = get_user_model()

def get_accessible_users(user):
    """return all other users the given user is allowed to contact
    """
    users = User.objects.exclude(pk__lte=1)
    users = users.exclude(pk=user.pk)
    users = users.filter(is_active=True)
    # if user is manager or admin: return all users
    if user.is_superuser or user.collab.is_manager:
        return users
    # else: return only the group members the user is itself a member of
    accessible_spaces = get_accessible_spaces(user)
    users = users.filter(groups__name__in=["%s: Members" % str(space.pk) for space in accessible_spaces])
    return users