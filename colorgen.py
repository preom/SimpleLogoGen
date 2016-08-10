from showPalette import PaletteGen

class ColorGen:

    def __init__(self, text=''):
        """ Deterministic generation of color based on seed 
        
            Args:
                text (str): Textual seed

        """
        self.text = text
        self.clear()

    def HGen(self):
        """ Generate the Hue value 
        
            Returns:
                int 

        """
        if(self.h):
            return self.h

        letters = [ord(i) for i in self.text]
        result = sum(letters) % 360

        self.h = result

        return result

    def SGen(self):
        """ Generate the Saturation value
        
            Returns:
                float

        """
        if (self.s):
            return self.s

        result = 0.5

        self.s = result

        return result

    def LGen(self):
        """ Generate the Light value 
        
            Returns:
                float

        """
        if (self.l):
            return self.l

        result = 0.3

        self.s = result

        return result

    def setText(self, text):
        """ Change seed value 
        
            Args:
                text (str): New text value

        """
        self.text = text
        self.clear()
    
    def clear(self):
        """ Clears cached information
        
        """
        self.h = None
        self.s = None
        self.l = None

    def generateHSL(self, strOutput=False):
        """ Generate a hsl value.
            
            Args:
                strOutput (bool): If Output should be a string. Defaults to False.

            Returns:
                list of int or str in format "hsl(x, x%, x%)"
                
        """
        h, s, l = self.HGen(), self.SGen(), self.LGen()

        if (strOutput):
            output = "hsl({}, {}%, {}%)".format(h, int(s * 100), int(l * 100))
        else:
            output = (h, s, l)

        return output

if __name__ == "__main__":
    CGen = ColorGen('luwak')

    textValues = ['bye', 'luwak', 'startup', 'this', 'that', 'dog', 'maestro']

    outputValues = []

    for i in textValues:
        CGen.setText(i)
        outputValues.append(CGen.generateHSL(strOutput=True))

    PG = PaletteGen(outputValues)
    PG.show()







