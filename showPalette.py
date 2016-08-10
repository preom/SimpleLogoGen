from PIL import Image, ImageDraw

class PaletteGen:
    def __init__(self, colors):
        """ Class for working with color palettes 
            
            Args:
                colors (int): List of color values. Should be compatible with PIL

        """ 

        self.colors = colors

        self.sW = 30 # sampleWidth
        self.sH = 30 # sampleHeight
        self.padding = 5

    def show(self):
        """ Visual representation of palette 
        
            Note:
                Relies on PIL

        """
        tPadding = (len(self.colors) + 1) * self.padding #total Padding

        img = Image.new('RGB',(len(self.colors) * self.sW + tPadding, self.sH), 'white')
        draw = ImageDraw.Draw(img)

        for i, c in enumerate(self.colors):
            x0, y0 = i * (self.sW + self.padding) + self.padding, 0
            x1, y1 = x0 + self.sW, y0 + self.sH

            draw.rectangle([x0, y0, x1, y1], fill=c)

        img.show()
    
if __name__ == "__main__":        
    PG = PaletteGen(['red', 'blue', 'green'])
    PG.show()


