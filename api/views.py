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
import base64

# Create your views here.

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def encode_image(output):
    ''' This encodes bytes to 64 encoding'''
    return base64.b64encode(output)

def compress_image(input_image_path, quality=90):
    ''' Compresses image from path and return 64 encoded bytes.
    '''
    output = BytesIO()

    image =  PILImage.open(input_image_path)
    image.save(output, "PNG", optimize=True, quality=quality)
    
    # output = encode_image(output.getvalue())
    return output

def decompress_image(input_image_path):
    ''' Decompresses image from path and return 64 encoded bytes.
    '''
    output = BytesIO()
    
    image = PILImage.open(input_image_path)
    image.save(output, "PNG")
        
    # output = encode_image(output)
    return output


def handle_upload_file(f):
    #Take image file and save locally to `img.jpg`
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class CompressImageAPIView(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        
        try:
            # compressed_image = Image(request.POST, request.FILES)
            # if form.is_valid():
            img = request.FILES['image']
            if img:
                handle_upload_file(img)
            
            image_file = 'img.jpg'
            
            output = compress_image(image_file).getvalue()
            output = encode_image(output)
                        
            result = {
                "base64EncodedBytes" : output
            }
                                    
            return Response(result, status=status.HTTP_200_OK)
            # return Response(request.POST, status=status.HTTP_200_OK)
            # return Response(output, status=status.HTTP_200_OK, content_type="image/png")
        
        except Exception as e:
            
            return Response(f'Exception while saving image: {e}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DecompressImageAPIView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            # compressed_image = Image(request.POST, request.FILES)
            # if form.is_valid():
            img = request.FILES['image']
            if img:
                handle_upload_file(img)
            
            image_file = 'img.jpg'
            
            output = decompress_image(image_file).getvalue()
            output = encode_image(output)
                        
            result = {
                "base64EncodedBytes" : output
            }
                                    
            return Response(result, status=status.HTTP_200_OK)
            # return Response(request.POST, status=status.HTTP_200_OK)
            # return Response(output, status=status.HTTP_200_OK, content_type="image/png")
    
        except Exception as e:
            
            return Response(f'Exception while saving image: {e}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Decompress
class GetThumbnailAPIView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def home(request):
    return render(request, 'home.html')

