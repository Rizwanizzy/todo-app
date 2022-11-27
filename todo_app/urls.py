from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homelistview/', views.HomeListView.as_view(), name='homelistview'),
    path('homeupdateview/<int:pk>/', views.HomeUpdateView.as_view(), name='homeupdateview'),
    path('homedetailview/<int:pk>/', views.HomeDetailView.as_view(), name='homedetailview'),

]
