import os
from directory import Directory
from file import File


def draw_files_system(folder_path, space = ''):

    folder_name = os.path.basename(folder_path)
    directory = Directory(folder_name)
    directory.draw(space)

    for item in os.listdir(folder_path):
        full_path =  os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            subdir = Directory(item)
            directory.add_child(subdir)

            if not item.startswith('.') and not item.startswith('__'):
                draw_files_system(full_path, space + ' ' * 4)

        else:
                size = os.path.getsize(full_path)
                file = File(item, size)
                directory.add_child(file)
                file.draw(space + ' ' * 4)


    return directory
