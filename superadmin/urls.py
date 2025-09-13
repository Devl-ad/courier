from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="admindashboard"),
    path("sign-out/", views.sign_out, name="sign_out"),
    path("packages/", views.packages_list, name="packages_list"),
    path("packages/<int:pk>/", views.packages_detail, name="packages_detail"),
    path("new-package/", views.new_packages, name="new_package"),
    path("send-mail/", views.send_message, name="send_message"),
]
