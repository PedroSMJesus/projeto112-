import os
import shutil

from_dir = "C:/Users/DELL/Desktop/Byjus/imagens"
to_dir = "C:/Users/DELL/Arquivos_documentos"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in [".gif", ".png", ".jpeg", ".jpg", ".jfif"]:
        path1 = from_dir + "/" + file_name 
        path2 = to_dir + "/" + "image_files"
        path3 = to_dir + "/" + "image_files" + "/" + file_name
    
    
    if os.path.exists(path2): 
        print("Moving " + file_name + ".....") 
        # Move from path1 ---> path3 
        shutil.move(path1, path3) 
    else: 
        os.makedirs(path2) 
        print("Moving " + file_name + ".....") 
        shutil.move(path1, path3)           
