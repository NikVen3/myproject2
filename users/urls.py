from django.urls import path, include
from django.views.generic import TemplateView
from users.views import Register, CustomPasswordResetDoneView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('accounts/password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('home/', TemplateView.as_view(template_name='cocktail/home.html'), name='home'),
]