import os
from subprocess import Popen,PIPE

path = os.getcwd()
files = os.listdir(path)
directory = []

for file in files:
  if(file[0] != '.'):
    print(file)
    directory.append(file)


process = Popen(['python', 'pointers.py'],stdout=PIPE)
for line in process.stdout:
  print(line)


