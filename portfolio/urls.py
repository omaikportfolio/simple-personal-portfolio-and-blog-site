from django.urls import path
from . import views
app_name = 'portfolio'

urlpatterns = [
    path('proj/', views.ProjectList.as_view(), name = 'proj_list'),
    path('proj/<int:pk>', views.ProjectDetail.as_view(), name = 'proj_detail')
]
