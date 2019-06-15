from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-blog/', views.all_blog, name='all-blog'),
    path('recent-stories/', views.recent_stories, name='recent-stories'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('single-post/', views.single_post, name='single-post'),
    path('single-post/<int:pk>/', views.post_detail, name='post-detail'),
]