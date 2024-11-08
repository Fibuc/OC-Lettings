from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.test_error_404, name='404'),
    path('500/', views.test_error_500, name='500'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
