#3. baemin/urls.py파일에서 복사하고나서 admin부분은 지운다

from django.conf.urls import url, include
from .views import (
    index,
    edit_info,
    signup, login, logout, #auth
    menu, menu_add,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^edit/$', edit_info, name='edit'),
    url(r'^menu/$', menu, name='menu'),
    url(r'^menu/add/$', menu_add, name='menu_add'),
]
