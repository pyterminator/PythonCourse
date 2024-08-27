import os 
import shutil

# Current Working Directory
BASE_DIR = os.getcwd()
 

folder_name = "Test"
folder_path = os.path.join(BASE_DIR, folder_name) 

# if os.path.exists(folder_path):
#     print("Var")
# else:
#     os.mkdir(folder_path)
#     print("Yoxdur")

# if os.path.exists(folder_path):
#     os.rmdir(folder_path)
#     print("Silindi")
# else:
#     print("Yoxdur")

# if os.path.exists(folder_path):
#     shutil.rmtree(folder_path)
#     print("Silindi")
# else:
#     print("Yoxdur")

# fayllar_folderler = os.listdir(folder_path)
# fayllar_folderler = [os.path.join(folder_path, element) for element in fayllar_folderler]

# # print(fayllar_folderler)
# for element in fayllar_folderler:
#     if os.path.isdir(element):
#         os.rmdir(element)
#     else:
#         os.remove(element)
# os.rmdir(folder_path)

# file_name = "base.py"
# file_path = os.path.join(BASE_DIR, file_name)

# if os.path.exists(file_path):
#     print("Var")
# else:

#     file = open(file_path, "x") 
#     file.close()



