from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
image_path="certificates/webinartemplate.png"
img = Image.open(image_path)
names= os.environ.get("PARTICIPANTS").split(',')
orgin=(2334/2 ,920)
font_size=90
font_color=(0,0,0)
font = ImageFont.truetype('fonts\Montserrat-Medium.ttf', int(font_size*1.33333))
print(names)
for data in names:
    img = Image.open(image_path)
    drawer = ImageDraw.Draw(img)
    drawer.text(orgin, data, font=font, fill = font_color,anchor="ms")
    path=str("certificates/"+data.replace("."," ")+".png")
    print(path)
    img.save(path)