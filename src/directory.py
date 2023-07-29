import os
import error_message as EM


def directory_exists(directory_path):
    return os.path.exists(directory_path)


def create_directory(directory_path):
    if directory_exists(directory_path):
        EM.showErrorPopUp("The directory already exists.")
        return
    try:
        os.makedirs(directory_path)
    except OSError as error:
       EM.showErrorPopUp("Error creating directory. Please check try again later") 


