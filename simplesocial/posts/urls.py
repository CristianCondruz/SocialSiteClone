from django.urls import path, re_path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    re_path('by/(?P<username>[-w]+)/$', views.UserPosts.as_view(),name='for_user'),
    re_path('by/(?P<username>[-w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    path('delete/(?P<pk>\d+)/$', view.DeletePost.as_view(), name = 'delete'),
]
