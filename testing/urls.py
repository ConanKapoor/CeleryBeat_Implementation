#Author - Shivam Kapoor

#Importing Essentials
from django.conf.urls import url
from testing import views

#Forming URLs
urlpatterns = [
    url(r'^$', views.url_retrieval, name='userdata'),
]
