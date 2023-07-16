import customtkinter
import tkinter as tk
from PIL import ImageTk, Image

class Home(customtkinter.CTk):
    """
        A class used to create the home window

        Methods
        __________

        initialiseWidget()
            Initialize and create all widgets necessary for the home window. 
            This includes the window, titleLabel, and the startButton
            This window will use the DaynNight theme provided by ctk_theme_builder 
            created by avalon60

        start()
            Will create an extra window
            
    """
    def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        customtkinter.set_default_color_theme("theme/DaynNight.json")
        self.geometry("500x200")
        self.title("Budget Visualiser")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Budget Visualiser", font = ("American Typewriter",40))
        titleLabel.grid(row = 1, column = 0, padx = 20, pady = 20)
        startButton = customtkinter.CTkButton(self, text = "Start", command = self.start)
        startButton.grid(row = 3, column = 0, padx = 20, pady = 20)
    
    def __init__(self):
        #super().__init__ basically calls customtkinter.CTK's constructor
        super().__init__() 
        self.initialiseWidget()
    
    #TODO: think about how you want to implement this to smoothen the flow of the application
    def start(self):
        print("Hello World")
