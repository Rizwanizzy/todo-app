from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homelistview/', views.HomeListView.as_view(), name='homelistview'),
    path('homeupdateview/<int:pk>/', views.HomeUpdateView.as_view(), name='homeupdateview'),
    path('homedetailview/<int:pk>/', views.HomeDetailView.as_view(), name='homedetailview'),
    path('homedeleteview/<int:pk>/', views.HomeDeleteView.as_view(), name='homedeleteview'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
