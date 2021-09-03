from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('chart', views.PostChartView.as_view(), name='post_chart'),
    path('<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/',views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(), name='post_delete')
]
