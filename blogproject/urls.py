from django.conf.urls import include, url
from django.contrib import admin
import blog.urls
from blog.views import index, login, login_acc, logout, sub_page
from blog.views import p_china, p_usa
urlpatterns = [
    url(r'^blog/$', index),
    url(r'^china/$', p_china),
    url(r'^usa/$', p_usa),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^login_acc/', login_acc),
    url(r'^logout/', logout),
    url(r'^blog/(?P<bbs_id>\d)', sub_page),
]