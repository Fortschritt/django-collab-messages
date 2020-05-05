from django.conf.urls import url
from . import views


app_name="collab_messages"
urlpatterns = [
    url(r"^inbox/$", views.CollabInboxView.as_view(),
        name="inbox"),
    url(r"^create/$", views.CollabMessageCreateView.as_view(),
        name="message_create"),
    url(r"^create/(?P<user_id>\d+)/$", views.CollabMessageCreateView.as_view(),
        name="message_user_create"),

    url(r"^thread/(?P<pk>\d+)/$", views.CollabThreadView.as_view(),
        name="thread_detail"),
    url(r"^thread/(?P<pk>\d+)/delete/$", views.CollabThreadDeleteView.as_view(),
        name="thread_delete"),
]