from django.urls import path

from .views import  *
urlpatterns = [
    path('list/',Car_list_view,name = 'list'),
    path('list/<int:pk>/',Car_detail_view,name = 'details'),
]