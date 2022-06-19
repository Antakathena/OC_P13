from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    print(f"{division_by_zero} : Ceci est une erreur volontaire pour tester Sentry")


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include("lettings.urls", namespace='lettings')),
    path('profiles/', include("profiles.urls", namespace='profiles')),

    # path('lettings/', views.lettings_index, name='lettings_index'),
    # path('lettings/<int:letting_id>/', views.letting, name='letting'),
    # path('profiles/', views.profiles_index, name='profiles_index'),
    # path('profiles/<str:username>/', views.profile, name='profile'),

]
