

from django.urls import include, path
from django.conf.urls.static import static
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'), 
    path('<int:blog_id>/', views.detail, name='detail'),
]