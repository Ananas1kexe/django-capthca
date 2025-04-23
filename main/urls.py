from django.urls import path
from . import views



urlpatterns = [
    path("", views.main, name="captcha"),
    path("index/", views.index, name="index"),
    path('captcha-image/', views.captcha_image, name='captcha_image'),
    path('verify/', views.captcha_verify, name='captcha_verify'),

]