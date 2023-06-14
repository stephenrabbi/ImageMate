from django.urls import path, include
from .views import *

# api/

urlpatterns = [
    # path('images', ImageListCreateAPIView.as_view(), name='image-list-create'),
    # path('images/<int:pk>', ImageRetrieveUpdateDestroyAPIView.as_view(), name='image-retrieve-update-destroy'),
    path('compress_image', CompressImageAPIView.as_view(), name='compress-image'),
    path('decompress_image', CompressImageAPIView.as_view(), name='decompress-image'),
    path('', home, name='home'),
    # path('get_thumbnail/<int:pk>', GetThumbnailAPIView.as_view(), name='get-thumbnail'),
]   
