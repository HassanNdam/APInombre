from django.urls import path
from .views import AdditionView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('addition/', AdditionView.as_view(), name='addition'),
    path('admin/', admin.site.urls),
    path('api/', include('monapp.urls')),
    path('catalog/', include('catalog.urls')),
    path('', views.index, name='index')
]