from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

