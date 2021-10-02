from PIL import Image, ImageDraw, ImageFont
import random

font = ImageFont.truetype('OpenSansEmoji.ttf', 400, encoding='unic')   
e = (random.choice(open('emojis2.txt',encoding='utf-8').readline().split()))

for x in range(0,1):
        canvas = Image.new('RGBA', (500,500), (random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256)))
        draw = ImageDraw.Draw(canvas)
        w, h = draw.textsize(e, font=font)
        h += int(h*0.21)
        draw.text(((500-w)/2, (500-h)/2), e, font=font, fill=(random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256)))
        canvas.show()
