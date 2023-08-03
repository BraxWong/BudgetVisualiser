import customtkinter
import tkinter as tk
import new_account as NA
from tkinter import messagebox
class Login(customtkinter.CTk):

    def __init__(self):
        self.username = "Something"
        self.password = "Something"
        super().__init__()
        self.initialiseWidget()

    def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        customtkinter.set_default_color_theme("../theme/DaynNight.json")
        self.geometry("500x400")
        self.title("Budget Visualiser Login")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="User Login", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, padx = 20, pady = 20)
        ForgetPasswordButton = customtkinter.CTkLabel(self,text="Forget Password?", font = ("American Typewriter",25))
        ForgetPasswordButton.grid(row = 4, column = 0, padx = 20, pady = 20)
        username = customtkinter.CTkTextbox(master = self, height = 20, width = 150)
        username.grid(row = 1, column = 0, padx = 20, pady = 20)
        password = customtkinter.CTkTextbox(master = self, height = 20, width = 150)
        password.grid(row = 2, column = 0, padx = 20, pady = 20)
        LoginButton = customtkinter.CTkButton(self, text = "Log In", command = lambda: self.login(username.get("0.0","end"),password.get("0.0","end")))
        LoginButton.grid(row = 3, column = 0, padx = 20, pady = 20)

    def login(self, username, password):
        self.username = username 
        self.password = password 
        if self.AccountVerification(self.username, self.password):
            print("Success")
        else:
            messagebox.showinfo("PopUp", "The username or password you have provided is not correct. Please try again.")

    def AccountVerification(self, username, password):
        print(username)
        print(password)
        LoginDetails = NA.NewAccount()
        if LoginDetails.accountExists(username):
            usernameTXT = open("../user_info/username.txt", "r")
            passwordTXT = open("../user_info/password.txt", "r")
            usernameIndex = 0
            passwordIndex = 0
            for x in usernameTXT:
                if x == username:
                    break
                ++unsernameIndex
            for y in passwordTXT:
                if y == password and passwordIndex == usernameIndex:
                    return True
                ++passwordIndex
        else:
            return False
        return True
