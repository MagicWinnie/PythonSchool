import os
from shutil import copyfile

direct = "Lesson_5"

files = os.listdir(direct)
os.mkdir(direct+"_converted")

for i in range(len(files)):
    copyfile(direct+"/"+files[i], direct+"_converted" + "/" + files[i][:2] + "txt")
