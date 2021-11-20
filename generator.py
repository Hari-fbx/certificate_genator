from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
img = Image.open('webinartemplate_withoutname.png')
data="Hari Krishna M"
orgin=(2049 ,2442)
font_size=180
font_color=(0,0,0)
drawer = ImageDraw.Draw(img)
font = ImageFont.truetype('fonts\Montserrat-Medium.ttf', font_size)
drawer.text(orgin, data, font=font, fill = font_color)
path=str("certificates/"+data+".png")
img.save(path)