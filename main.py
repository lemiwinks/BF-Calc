from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
import math

saveList = []

class MainScreen(Screen):
    

    def goCalc(self):
        bf = 'False'
        lf = 'False'
        w = float(self.ids.widthInput.text)
        l = float(self.ids.lengthInput.text)
        t = float(self.ids.thicknessInput.text)
        cost = float(self.ids.cost.text)
        if self.ids.bf.active:
            bf = 'True'
            lf = 'False'
        elif self.ids.lf.active:
            lf = 'True'
            bf = 'False'
        costbf = ((w*l*t)/12)*cost
        costlf = l*cost
        if self.ids.bf.active:
            self.ids.totalCost.text = str(costbf)
        elif self.ids.lf.active:
            self.ids.totalCost.text = str(costlf)
        

    def goFigure(self):
        # width (width of the board)
        width = float(self.ids.widthInput.text)

        # widthp (width of the pieces)
        widthp = float(self.ids.widthOfPiece.text)+.375

        # length (length of the board)
        length = float(self.ids.lengthInput.text)*12

        # lengthp (length of the pieces)
        lengthp = float(self.ids.lengthOfPiece.text)+.375

        # numneed (number of pieces needed)
        #numneed = float(self.ids.amountNeeded.text)

        # Pieces width-wise
        currentMeasureW = 0
        piecesCountW = 0
        while (currentMeasureW<=width):
            piecesCountW += 1
            currentMeasureW += widthp
        # Pieces length-wise
        currentMeasureL = 0
        piecesCountL = 0
        while (currentMeasureL<=length):
            piecesCountL += 1
            currentMeasureL += lengthp

        # Total Pieces
        total = piecesCountW*piecesCountL
        self.ids.pieces.text = str(total)

        if (self.ids.totalCost.text != ""):
            self.ids.pricePerPiece.text = str(float(self.ids.totalCost.text)/total)

    def addList(self):
        global saveList

        number = float(self.ids.pricePerPiece.text)
        step = math.floor(number*100)
        final = step/100

        list1 = [self.ids.widthInput.text,
                self.ids.lengthInput.text, 
                self.ids.thicknessInput.text,
                self.ids.totalCost.text,
                self.ids.pieces.text,
                str(final)
                ]
        saveList.append(list1)
        

        
        

class AboutScreen(Screen):

    def test(self):
        print (saveList)
        for x in saveList:
            textList = x[0] + '"x' + x[1] + "'x" + x[2] + '" @ $' + x[3] + ' = $' + x[4] + ' Total $' + x[5] + " per Piece"
            #textList = "Words"
            l = Label(text=textList)
            self.ids.printout.add_widget(l)
    def clearAll(self):
        self.ids.printout.clear_widgets()
        pass
    def clearBtn(self):
        global saveList
        self.ids.printout.clear_widgets()
        saveList = []

    pass


class ScreenManagement(ScreenManager):
    pass

Window.size = (1440,2960)

# Main Run Statements

class WinerackApp(App):


    pass

if __name__ == '__main__':
    WinerackApp().run()

