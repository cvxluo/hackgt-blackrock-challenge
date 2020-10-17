from PIL import Image

im = Image.open('imageEmbedded.png')
width, height = im.size
for x in range(width) :
    for y in range(height) :
        
        pixel = im.getpixel((x, y))
        if (pixel != (3, 3, 3) and pixel != (255, 255, 255)) :
            im.putpixel((x, y), (0, 255, 0))

im.show()