from PIL import Image, ImageDraw, ImageFont
import random

#font = ImageFont.truetype('OpenSansEmoji.ttf', 400, encoding='unic')   
#font = ImageFont.truetype('Symbola.ttf', 400, encoding='unic')

for x in range(0,1000):
        number = str(x).zfill(4)
        e = (random.choice(open('emojis2.txt',encoding='utf-8').readline().split()))
        canvas = Image.new('RGBA', (500,500), (random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256)))
        draw = ImageDraw.Draw(canvas)
        w, h = draw.textsize(e, font=font)
        h += int(h*0.21)
        draw.text(((500-w)/2, (500-h)/2), e, font=font, fill=(random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256)))
        #canvas.show()
        #print (e)
        #canvas.save("V:/NFT/EMOJIS/SYMBOLA/"+number+".png")