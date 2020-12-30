
from django.urls import path
from .views import HomeView, ArticalDetailView, AddPostView, AddCommentView, LikeView,AddCategoryView,UpdatePostView,DeletePostView

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticalDetailView.as_view(), name='artical_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('artical/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('artical/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('artical/<int:pk>/delete', DeletePostView.as_view(), name="delete_post")
]