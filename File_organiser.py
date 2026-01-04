import os
import shutil
path = r"C:\Users\sasha\Downloads"
folder_dir = {'docs' : ['.txt','.pdf','.docx','.ppt', '.csv'],
              'media' : ['.mp3', '.png', '.jpg', '.jpeg', '.mp4', '.wav'],
              'zips' : ['.zip'],
              'apps' : ['.exe']}

file_list = os.listdir(path)
# file list will have all the items in the folder or the path given
for file in file_list:
    if os.path.isdir(os.path.join(path,file)):
        continue

    file_name, file_ext = os.path.splitext(file)
    moved = False
    for folder,values in folder_dir.items():
        if file_ext in values:
            new_folder_path = os.path.join(path,folder)
            os.makedirs(new_folder_path, exist_ok= True)
            old_file_path = os.path.join(path,file)
            new_file_path = os.path.join(new_folder_path,file)
            shutil.move(old_file_path,new_file_path)
            moved = True
            print(f'moved {file} to {folder} ; the new path - {new_folder_path}')
            break

    if not moved:
        misc_folder_path = os.path.join(path,'misc')
        os.makedirs(misc_folder_path, exist_ok=True)
        old_misc_file_path = os.path.join(path,file)
        new_misc_file_path = os.path.join(misc_folder_path,file)
        shutil.move(old_misc_file_path,new_misc_file_path)
        print(f'moved {file} to misc; the new path - {misc_folder_path}')
