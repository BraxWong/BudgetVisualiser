import customtkinter
import directory as DIR
import PopUpMessage as PM
import tkinter as tk
from tkinter import messagebox
class NewAccount(customtkinter.CTkToplevel):

     """
        A class used to create a window which allows users to create an account

        Methods
        __________

        initialiseWidget()
            Initialize and create all widgets necessary for the window. 
            This includes the window, newAccountLabel, username textbox, 
            password textbox, and the register Button This window will use 
            the DaynNight theme provided by ctk_theme_builder created by avalon60

        createAccount()
            This will create a directory called user_info at the project root,
            it will then open both username.txt and password.txt. It will then call 
            accountExists() method to check if the account already exists within the system.
            If so, an error message will be displayed and the account will not be registered.
            Else, the username and password will be registered (written) to the system. A pop up
            message will be displayed, saying the account has been registered successfully.

        accountExists()
            This will open the username.txt file to be read. It will then iterate through
            the file, and compate each line to find out whether the username is already present
            within the system (file)
    """

    def __init__(self):
        super().__init__()
        self.initialiseWidget()

    def createAccount(self, username, password):
        directory = DIR.Directory()
        directory.create_directory("../user_info")
        usernameTXT = open("../user_info/username.txt", "a")
        passwordTXT = open("../user_info/password.txt", "a")
        if not self.accountExists(username):    
            usernameTXT.write(username)
            usernameTXT.close()
            passwordTXT.write(password)
            passwordTXT.close()
            messagebox.showinfo("PopUp","Registeration Complete.")
        else:
            messagebox.showinfo("PopUp","Error. Account already exists within the system.")

    def accountExists(self, username):
        usernameTXT = open("../user_info/username.txt","r")
        for x in usernameTXT:
            if x == username:
                usernameTXT.close()
                return True
        return False       

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
        submit = customtkinter.CTkButton(self, text = "Create Accout", command = lambda: self.createAccount(username.get("0.0","end"),password.get("0.0","end"))) 
        submit.grid(row = 3, column = 0, padx = 20, pady = 20)
