from django.urls import include, path
from rest_framework import routers
from album_photoapp import views


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'photos', views.PhotoViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
