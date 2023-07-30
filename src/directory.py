import os
import PopUpMessage as PM

class Directory:

    def __init__(self):
        return

    def directory_exists(self, directory_path):
        return os.path.exists(directory_path)


    def create_directory(self, directory_path):
        if not self.directory_exists(directory_path):
            try:
                os.makedirs(directory_path)
            except OSError as error:
                PopUp = PM.MessagePopUp("There is an error when creating" + directory_path + ", please try again later.")

