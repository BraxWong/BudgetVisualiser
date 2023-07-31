import customtkinter

#DEPRECATED

class MessagePopUp(customtkinter.CTkToplevel):

    def __init__(self, Message):
        self.Message = Message
        super().__init__()
        self.initialiseWidget()

    def initialiseWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.resizable(False,False)
        customtkinter.set_default_color_theme("../theme/DaynNight.json")
        self.geometry("300x300")
        PopUpMessageLabel = customtkinter.CTkLabel(self, text = self.Message)
        PopUpMessageLabel.grid(row = 1, column = 0, padx = 20, pady = 20)
        ClosePopUpWindowButton = customtkinter.CTkButton(self, text = "Close", command = self.withdraw())
        ClosePopUpWindowButton.grid(row = 2, column = 0, padx = 20, pady = 20)

