import os
from folder import Folder
from file import File

def list_files_recc(folder_path) -> "Folder":

    folder_name = os.path.basename(folder_path)
    current_folder = Folder(folder_name)

    for item in os.listdir(folder_path):

        full_path = os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            if not item.startswith('.') and not item.startswith('__'):
            # FOLDER
                folder_comp = list_files_recc(full_path)
                current_folder.add_child(folder_comp)
        else:
            # FILE
            size = os.path.getsize(full_path)
            file = File(item, size)
            current_folder.add_child(file)

    return current_folder

