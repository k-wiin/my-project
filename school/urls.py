

from django.contrib import admin
from django.urls import path
from .import views
from rest_framework.routers import SimpleRouter
from rest_framework import routers

router = SimpleRouter()
# router = routers.DefaultRouter()
# router.register(r'students', views.studentset , basename='students')


urlpatterns = [
    path('',views.index),
    path('details/',views.db_save, name='details'),
    path('delete/',views.delet),
    path('search/',views.search),
    path('all/',views.all),
    path('get_all/',views.get_all),
    path('info/',views.apis.as_view({'post':'info'})),
    path('all_data/',views.all_data.as_view(),name='all_data')
    # path('views/', views.GeeksList.as_view())
]