import customtkinter
from tkinter import *
from PIL import Image

class Home(customtkinter.CTk):
    def __init__(self):
        #super().__init__ basically calls customtkinter.CTK's constructor
        super().__init__()
        self.geometry("600x500")
        self.title("Budget Visualiser")
        backgroundImage = customtkinter.CTkImage(light_image = Image.open("hero-BankingSaving-BudgetPlanner.jpg"), dark_image = Image.open("hero-BankingSaving-BudgetPlanner.jpg"),size=(130,130))
        backgroundImageLabel = customtkinter.CTkLabel(self, image = backgroundImage, text = "Background Image")
        startButton = customtkinter.CTkButton(self, text = "Start", command = self.button_event, hover = True, fg_color = "grey", text_color = "blue")
        startButton.grid(row = 4, column = 2, padx = 20, pady = 20)

    def button_event(self):
        print("Hello World")
