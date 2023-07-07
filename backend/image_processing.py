```python
from PIL import Image, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, meme):
        self.meme = meme

    def add_caption(self, text, font_size, color, position):
        image = Image.open(self.meme['path'])
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', font_size)
        draw.text(position, text, fill=color, font=font)
        image.save(self.meme['path'])

    def apply_filter(self, filter_name):
        image = Image.open(self.meme['path'])
        if filter_name == 'black_and_white':
            image = image.convert('L')
        elif filter_name == 'sepia':
            image = image.convert('RGB')
            pixels = image.load()
            for y in range(image.size[1]):
                for x in range(image.size[0]):
                    r, g, b = image.getpixel((x, y))
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                    pixels[x, y] = (tr,tg,tb)
        elif filter_name == 'pixelate':
            image = image.resize((image.size[0]//10, image.size[1]//10), Image.NEAREST)
            image = image.resize((image.size[0]*10, image.size[1]*10), Image.NEAREST)
        image.save(self.meme['path'])
```