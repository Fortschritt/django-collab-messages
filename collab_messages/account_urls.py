from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [
    # pinax_messages needs 'account', which overwrites login redirect behaviour
    # we don't want that and overwrite account's path with the one from django auth
    url(r'accounts/login/', login, name="account_login"),
]