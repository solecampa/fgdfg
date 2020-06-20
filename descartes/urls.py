from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.descartes, name="descartes"),
    path("descaraga", views.descaraga, name="descaraga"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("formulario", views.formulario, name="formulario"),
    path("remove", views.remove, name="remove"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="descartes/password_reset.html"), name="reset_password"),
    path("accounts/password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="descartes/password_sent.html"), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="descartes/reset_form.html"), name="password_reset_confirm"),
    path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="descartes/reset_done.html"),name="password_reset_complete")
    

]