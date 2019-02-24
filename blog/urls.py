from django.urls import path
from blog import views
app_name = 'blog'

urlpatterns = [
    path('blog/', views.ArticlesListView.as_view(), name = 'article_list'),
    path('blog/<int:pk>/', views.ArticlesDetail.as_view(),
                                                    name = 'article_detail'),
    path('blog/<int:pk>/comment', views.add_comment, name = 'add_comment')
]
