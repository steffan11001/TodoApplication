from django.urls import path,include
from rest_framework import routers
from rest_api import views
from rest_framework.authtoken import views as rest_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router= routers.DefaultRouter()
router.register(r'todoItem',views.TodoItemViewSet)

urlpatterns = [
    # your REST API urls
    # path('', ...),
    
    path('', views.ApiOverview, name='home'),
    path('',include(router.urls)),
    path('create/', views.add_todo_items, name='add-todo-items'),
    path('all/', views.view_todo_items, name='view-todo-items'),
    path('update/<str:title>/', views.update_todo_items, name='update-todo-items'),
    path('todoItem/<str:title>/delete/', views.delete_todo_items, name='delete-todo-items'),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/',TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('api-token-auth/',rest_views.obtain_auth_token),
]
