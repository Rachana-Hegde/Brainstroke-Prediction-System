from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name="index"),
    path('login/',views.user_login,name="login"),
    path('main',views.main,name="main"),
    path('prediction', views.prediction, name='prediction'),
    path('otpVerify',views.otpVerify, name="otpVerify"),
]