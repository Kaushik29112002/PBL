import os
import shutil

path = input('Enter path:')
files = os.listdir(path)

for file in files:
    if file.endswith(".docx") or file.endswith(".doc"):
        if not os.path.exists(path+'/Word'):
            os.makedirs(path+'/Word')
            shutil.move(path+'/'+file,path+'/Word')
        else:
             shutil.move(path+'/'+file,path+'/Word')

    if file.endswith(".txt"):
        if not os.path.exists(path+'/Text'):
            os.makedirs(path+'/Text')
            shutil.move(path+'/'+file,path+'/Text')
        else:
            shutil.move(path+'/'+file,path+'/Text')

    if file.endswith(".py") or file.endswith(".ipynb"):
        if not os.path.exists(path+'/Python'):
            os.makedirs(path+'/Python')
            shutil.move(path+'/'+file,path+'/Python')
        else:
            shutil.move(path+'/'+file,path+'/Python')

    if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):
        if not os.path.exists(path+'/IMAGES'):
            os.makedirs(path+'/IMAGES')
            shutil.move(path+'/'+file,path+'/IMAGES')
        else:
            shutil.move(path+'/'+file,path+'/IMAGES')
            
    if file.endswith(".mp4"):
        if not os.path.exists(path+'/VIDEOS'):
            os.makedirs(path+'/VIDEOS')
            shutil.move(path+'/'+file,path+'/VIDEOS')
        else:
            shutil.move(path+'/'+file,path+'/VIDEOS')

    
  
                                    
