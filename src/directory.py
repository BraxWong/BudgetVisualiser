import os
import error_message as EM

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
                EM.showErrorPopUp("Error creating directory. Please check try again later") 


