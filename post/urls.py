from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view()),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    path('post/<int:pk>/comment/create/', views.CommentCreateView.as_view(), name='comment_create'),

]
