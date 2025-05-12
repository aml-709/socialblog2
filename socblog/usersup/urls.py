from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from usersup import views
from usersup.views import (
    add_to_favorites, remove_from_favorites, favorites_view,
    post_list, post_detail, delete_post, toggle_like, toggle_dislike,
    profile_view, edit_profile, toggle_follow, account_view, Register
)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('account/', account_view, name='account'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/follow/', toggle_follow, name='toggle_follow'),
    path('Posts/create-post/', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('favorites/', favorites_view, name='favorites_view'),
    path('favorites/add/<int:post_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:post_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('register/', Register.as_view(), name='register'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('dislike/<int:post_id>/', toggle_dislike, name='toggle_dislike'),
    path('profile/<str:username>/posts/', views.user_posts, name='user_posts'),

    path('create_test_post/', views.create_test_post, name='create_test_post'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





