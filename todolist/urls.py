from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import *

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)
router.register(r'cat', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]
