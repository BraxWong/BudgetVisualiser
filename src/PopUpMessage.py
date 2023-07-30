import customtkinter

class MessagePopUp(customtkinter.CTkToplevel):

    message = ""

    def __init__(self, PopUpMessage):
        self.message = PopUpMessage
        super().__init__()
        self.initialiseWidget()

    def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.resizable(False,False)
        customtkinter.set_default_color_theme("../theme/DaynNight.json")
        self.geometry("200x200")
        PopUpMessageLabel = customtkinter.CTkLabel(self, text = self.message)
        PopUpMessageLabel.grid(row = 2, column = 0, padx = 20, pady = 20)
        ClosePopUpWindowButton = customtkinter.CTkButton(self, text = "Close", command = self.withdraw())


