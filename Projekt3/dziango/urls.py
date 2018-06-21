from django.conf.urls import url
from . import views
from django.contrib.auth import views as djviews

urlpatterns = [
    url(r"^$", views.threads, name="threads"),
    url(r'^thread/new/$', views.new_thread, name='new_thread'),
    url(r'^thread/(?P<pk>\d+)/$', views.thread_view, name='thread_view'),
    url(r'^signup/$', views.register, name='register'),
    url(r'^login/$', djviews.login, name='login'),
    url(r'^logout/$', djviews.logout, {'next_page': '/'}, name='logout'),
    url(r'^thread/(?P<pk>\d+)/post/new/$', views.new_post, name='new_post'),
    url(r'^thread/(?P<th_pk>\d+)/post/delete/(?P<pk>\d+)$', views.delete_post, name='delete_post'),
    url(r'^(?P<pk>\d+)/thread/delete/$', views.delete_thread, name='thread_delete'),
    url(r'^user/(?P<pk>\d+)/$', views.user, name='user_profile'),
    url(r'^user/edit/(?P<pk>\d+)/$', views.user_edit, name='user_edit'),

]
