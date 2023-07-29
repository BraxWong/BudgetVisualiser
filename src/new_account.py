import customtkinter

class NewAccount(customtkinter.CTkToplevel):

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

    def __init__(self):
        super().__init__()
        self.initialiseWidget()

    def createAccount(self, username, password):
        print(username)
        print(password)

    def accountExists():
        return True
        
