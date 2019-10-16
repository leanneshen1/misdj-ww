from django.urls import path
from . import views
app_name = 'note'

urlpatterns = [
    path('ww/', views.ww, name='ww'),
    path('init_ww/', views.init_ww, name='init_ww'),
    path('ww2/', views.ww2, name='ww2'),
    path('/', views.index, name='index'),
]