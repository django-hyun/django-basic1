from django.urls import path
from instagram import views

app_name = "instagram"

urlpatterns=[
    path('', views.post_list, name='post_list')
]

