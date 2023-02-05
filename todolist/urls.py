from django.contrib import admin
from django.urls import path, include

from todo.views import TodoAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/todos', TodoAPIView.as_view()),
    path('api/v1/todos/<int:pk>/', TodoAPIView.as_view()),
]
