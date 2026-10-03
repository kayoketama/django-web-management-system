from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("profile/", views.profile, name="profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-users/", views.admin_users, name="admin_users"),
    path(
    "admin-users/<int:user_id>/",
    views.admin_user_detail,
    name="admin_user_detail"
),
    path(
    "admin-users/<int:user_id>/delete/",
    views.admin_user_delete,
    name="admin_user_delete"
),
path(
    "admin-messages/",
    views.admin_messages,
    name="admin_messages"
),
path(
    "admin-messages/<int:message_id>/delete/",
    views.admin_message_delete,
    name="admin_message_delete"
),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
]