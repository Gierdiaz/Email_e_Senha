from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePagesView.as_view(), name='home'),
]