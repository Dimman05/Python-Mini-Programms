import gzip
import os
import shutil
from zipfile import ZipFile

result = []


def find_files(filename):
   result.clear()
   for root, dir, files in os.walk('c:\\'):
      if filename in files or filename in dir:
         result.append(os.path.join(root, filename))
   return result

def zip(file):
    with ZipFile(f'{file}.zip', 'w') as f:
        print('Zipping...')
        f.write(file)



def unzip(file):
    with ZipFile(file, 'r') as f_out:
        f_out.extractall('C:\\Users\\Dimitris\\Desktop')









