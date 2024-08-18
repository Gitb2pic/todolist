from django.urls import path
from .views import (
    CategoryListView,
    TaskListView,
    TaskUpdateView,
    CategoryCreateView,
    TaskCreateView
)

urlpatterns = [
    
    path("", CategoryListView.as_view(), name="home"),
    path('task/<int:pk>/', TaskListView.as_view(), name='task_detail'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path("create/category", CategoryCreateView.as_view(), name='category_create'),
    path("task/new", TaskCreateView.as_view(), name="task_new"),
    
]
