import os

for name in os.listdir(os.getcwd()):
    if ('.mp4'  not in name and'en' not in name):
        os.remove(name)


 
