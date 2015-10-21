from django.conf.urls import patterns, include, url
from django.contrib import admin
from motivatin import views
from django.views.generic import ListView
from motivatin.models import Task

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finalproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.Home.as_view(template_name="motivatin/home.html"), name='home'),
    url(r'^dashboard/', views.TaskList.as_view(template_name="motivatin/dashboard.html"), name='dashboard'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^add/tag/', views.TagCreate.as_view(), name='tag_add'),
    url(r'^add/$', views.TaskCreate.as_view(), name='task_add'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.TaskUpdate.as_view(),  name='task_update'),
    url(r'^task/(?P<pk>\d+)/', views.TaskDetail.as_view(), name='task_detail'),
)