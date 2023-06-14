from django.shortcuts import render
from rest_framework import generics, status
from .models import Image, User
from .serializers import ImageSerializer, UserSerializer
from django.urls import path
from PIL import Image as PILImage
from io import BytesIO
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
from .forms import ImageUploadForm

# Create your views here.

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



def compress_image(input_image_path, output_image_path, quality=90):
    with PILImage.open(input_image_path) as image:
        image.save(output_image_path, "JPEG", optimize=True, quality=quality)

def decompress_image(input_image_path, output_image_path):
    with PILImage.open(input_image_path) as image:
        image.save(output_image_path, "JPEG")


compressed_path = "compressed_image.jpg"
decompressed_path = "decompressed_image.png"

def handle_upload_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class CompressImageAPIView(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        try:
            print()
            
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                handle_upload_file(request.FILES['image'])
                
            output_file = 'out.jpg'
            # image_file = request.FILES.get('file')
            # image_file = request.data.get('file')
            # output_file = request.data.get('out_file') or compressed_path
            # compression_level = request.data.get('compression_level')
            
            result = compress_image('img.jpg', output_file)
            result = open(output_file, 'rb')
            
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(result, status=status.HTTP_200_OK)
        
        except Exception as e:
            
            return Response(f'Exception while saving image: {e}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DecompressImageAPIView(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        image_file = request.FILES.get('file')
        compression_level = request.data.get('compression_level')

        # Open the image file using Pillow
        image = PILImage.open(image_file)
        
        image.save(image_file, optimize=True)

        # Create a thumbnail for the compressed image
        thumbnail_size = (100, 100)
        image.thumbnail(thumbnail_size)
        thumbnail_io = BytesIO()
        image.save(thumbnail_io, format='JPEG')

        # Save the compressed image and thumbnail to the database
        compressed_image = Image(file=image_file, compression_level=compression_level)
        compressed_image.thumbnail.save(image_file.name, thumbnail_io, save=False)
        compressed_image.save()

        # Serialize the compressed image data
        serializer = self.get_serializer(compressed_image)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Decompress
class GetThumbnailAPIView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def home(request):
    return render(request, 'home.html')
