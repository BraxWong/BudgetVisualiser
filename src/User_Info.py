import new_account as NA
import tkinter as tk
import directory as DIR
from tkinter import messagebox

class user_info:
    """
        A class used to handle all things related to user information

        Methods
        __________

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

        login()
            This will call AccountVerification to find out whether the details inputted are 
            accurate. Then it will grant access to the system.

        AccountVerification()
            This will take the details being passed in, then find out whether the details are 
            matched with the info embedded into the system. Then it will return True if the details
            are correct. False if the details are not correct.
    """
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

   
    def login(self, username, password):
        if self.AccountVerification(username, password):
            print("Success")
        else:
            messagebox.showinfo("PopUp", "The username or password you have provided is not correct. Please try again.")


    def AccountVerification(self, username, password):
        if self.accountExists(username):
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
