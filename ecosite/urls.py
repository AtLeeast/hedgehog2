from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .api.signup import SignupApiView
from .api.signin import SigninService

app_name = 'ecosite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('statistics/', views.statistics, name='statistics'),
    path('api/quit/', views.quit, name='quit'),
    path('api/signup/', SignupApiView.as_view()),
    path('api/signin/', SigninService.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
