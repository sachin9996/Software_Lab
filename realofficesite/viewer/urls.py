from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name ='index'),
    url(r'^edit_favorites/',views.edit_favorites,name='edit_favorites'),
]
