import os
import sys

from tkinter import Tk
from tkinter import X,Y,BOTH
from tkinter import Text, Button,Label
from tkinter.ttk import Frame

from daysCalculatorCore import DaysCalculator


# Classe responsável por Controlar toda a interface e gestão de componentes do days calculator
class DaysCaculatorInterface(Tk):

    InputDays = Text
    btCalculate = Button
    lbResult = Label
    frameHome = Frame
    CalculatorObj = DaysCalculator

    def ConfigAppComponents(self):

        self.title("Days Calculator")

        self["bg"] = "#616161"

        self.Positioninthecenter()

        self.frameHome = Frame(self)
        self.frameHome.pack()

        self.InputDays = Text(self.frameHome,height=1)
        self.InputDays.pack(padx=40,pady=5)

        self.btCalculate = Button(self.frameHome)
        self.btCalculate["command"] = self.calculate        
        self.btCalculate["font"] = ("Roboto","10")
        self.btCalculate["text"] ="Calcular"
        self.btCalculate["fg"] = "white"
        self.btCalculate["bg"] = "#34A853"
        self.btCalculate["relief"] = "flat" 
        self.btCalculate.pack(fill=X,padx=40,pady=5)

        self.lbResult = Label(self.frameHome,height=9)
        self.lbResult.pack()

        self.CalculatorObj = DaysCalculator()

    def calculate(self):
        
        try:

            inputNumber = int(self.InputDays.get("1.0","end").replace('\n',''))
        except:

            return

        retorno = self.CalculatorObj.calculate(inputNumber)

        self.lbResult["text"] = "Para " + str(inputNumber) + " horas, o resultado é: \nData inicio: " + retorno[0] + "\nData fim: " + retorno[1]
        
    
    def Positioninthecenter(self):

        largura = 250
        altura = 200

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2

        self.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.minsize(200,200)