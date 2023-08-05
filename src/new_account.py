import customtkinter
import tkinter as tk
import User_Info as UI
class NewAccount(customtkinter.CTkToplevel):

     """
        A class used to create a window which allows users to create an account

        Methods
        __________

        initialiseWidget()
            Initialize and create all widgets necessary for the window. 
            This includes the window, newAccountLabel, username textbox, 
            password textbox, and the registerButton. This window will use 
            the DaynNight theme provided by ctk_theme_builder created by avalon60.
            When the registerButton is clicked, createAccount() from User_Info.py 
            will be called. For more information, please read User_Info documentation
    """

     def __init__(self):
        super().__init__()
        self.ui = UI.user_info()
        self.initialiseWidget()

     def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.resizable(False,False)
        customtkinter.set_default_color_theme("../theme/DaynNight.json")
        self.geometry("400x300")
        newAccountLabel = customtkinter.CTkLabel(self,text="Create a New Account", font = ("American Typewriter",25))
        newAccountLabel.grid(row = 0, column = 0, padx = 20, pady = 20)
        username = customtkinter.CTkTextbox(master = self, height = 20, width = 150)
        username.grid(row = 1, column = 0, padx = 20, pady = 20)
        password = customtkinter.CTkTextbox(master = self, height = 20, width = 150)
        password.grid(row = 2, column = 0, padx = 20, pady = 20)
        submit = customtkinter.CTkButton(self, text = "Create Accout", command = lambda: self.ui.createAccount(username.get("0.0","end"),password.get("0.0","end"))) 
        submit.grid(row = 3, column = 0, padx = 20, pady = 20)
