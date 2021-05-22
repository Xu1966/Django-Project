from django.conf.urls import include
from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^user/$',views.user,name='user'),
    url(r'^help/$',views.help,name='help'),
    url(r'^users/$',views.users,name='users'),
]
