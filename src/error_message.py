import customtkinter

class MessagePopUp(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.initialiseWidget()


    def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.resizable(False,False)
        customtkinter.set_default_color_theme("../theme/DaynNight.json")
        self.geometry("200x200")
 
def showErrorPopUp(errorMessage):
    return
