
from django.urls import path
from django.urls import reverse
from . import views
app_name= 'blog'
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # <int:year>/<int:month>/<int:day>/
    path('<slug:post>/', views.post_detail, name='post_detail'),
    # path('publish/post/list', views.publish_post_list),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share',views.post_share, name="post_share"),
    path('<int:post_id>/comment',views.post_comment, name="post_comment")

]
