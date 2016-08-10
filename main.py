from PIL  import Image, ImageDraw, ImageFont
from colorgen import ColorGen

def main():
    img = Image.new('RGB', (100,100))
    text = 'P'

    CG = ColorGen(text)
    
    font = ImageFont.truetype('arial.ttf', 80)
    fontMarginH = int((img.width - font.getsize(text)[0])/2)
    fontMarginV = int((img.height - font.getsize(text)[1])/3)

    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0, img.width, img.height], fill=CG.generateHSL(strOutput=True))
    draw.text((fontMarginH, fontMarginV), 'P', fill='white', font=font)

    img.show()
    

main()
