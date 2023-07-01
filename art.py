import sys
from PIL import Image
from termcolor import colored
import colorama
colorama.init()
try:
    image_path = sys.argv[1].strip('-')
except:
    image_path = 'test.jpg'
class AsciiArt:
    def __init__(self, img_path):
        self.path = image_path
        self.img = Image.open(self.path)

    def image(self):
            width, height = self.img.size
            aspect_ratio = height/width
            new_width = 120
            new_height = aspect_ratio * new_width * 0.55
            img = self.img.resize((new_width, int(new_height)))
            img = img.convert('L')
            pixels = img.getdata()
            chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
            new_pixels = [chars[pixel//25] for pixel in pixels]
            new_pixels = ''.join(new_pixels)
            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index:index + new_width]
                  for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)
            file = "ascii_image_full.txt"
            with open(file, "w") as f:
            	f.write(ascii_image)
            	print(colored(f"saved art image to file as {file}", "yellow"))
           
            
            
            
            
if __name__ == "__main__":
    AsciiArt(image_path).image()
