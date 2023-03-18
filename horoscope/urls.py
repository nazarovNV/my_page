from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('type/', views.get_types_of_zodiacs),
    path('type/<str:type_zodiac>/', views.get_info_about_type, name='type-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name')
]
