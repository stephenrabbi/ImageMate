from PIL import Image
import io

def compress_image(input_image_path, output_image_path, quality=90):
    with Image.open(input_image_path) as image:
        image.save(output_image_path, "JPEG", optimize=True, quality=quality)

def decompress_image(input_image_path, output_image_path):
    with Image.open(input_image_path) as image:
        image.save(output_image_path, "JPEG")

# Example usage
folder = 'image/'
input_path = "12.jpeg"

file = folder + input_path
compressed_path = "compressed_image.jpg"
decompressed_path = "decompressed_image.png"

# Compress the image
compress_image(file, compressed_path, quality=50)

# # Decompress the image
# decompress_image(compressed_path, decompressed_path)
