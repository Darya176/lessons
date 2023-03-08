"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os

def new_folder(folder_path):
    for folder_name in os.listdir(folder_path):
        if folder_name.isdigit():
            folder_num = int(folder_name)
            if folder_num % 2 == 0:
                rename = 'папка_' + str(folder_num)
                os.rename(os.path.join(folder_path, folder_name),
                          os.path.join(folder_path, rename))

target_path = 'target'
if os.path.exists(target_path):
    new_folder(target_path)