from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homelistview/', views.HomeListView.as_view(), name='homelistview'),


]
