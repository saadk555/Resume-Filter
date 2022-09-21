from audioop import reverse
import ocr
import glob
import os
import platform
from pathlib import Path
import shutil

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re

all_files = []

if platform.system() == "Windows":
	# We may need to do some additional downloading and setup...
	# Windows needs a PyTesseract Download
	# https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine

	pytesseract.pytesseract.tesseract_cmd = (r"D:\\Tesseract-OCR\\tesseract.exe")


path_to_poppler_exe = Path(r"C:\\Program Files\\poppler-0.68.0\bin")
		
find_word = ''

inpath = input('Please enter the file path:  ')

list_compare = []

words = int(input('How many words you want to find: '))

path = glob.glob('D:\python_workspaces\cv-man\*.pdf')

for num in range(words):

    string = input('Please enter the words you want to find: ')
    find_word += "\\b" + string + "\\b" + '|'
    
find_word = find_word[:-1]


for file in path:
    PDF_file = Path(fr"{file}")
    print(PDF_file)
    ocr.main(list_compare,find_word,PDF_file)
    all_files.append(file)


print(all_files)
'''
name = os.path.split(file)
basename.append(name[1])
'''
print(list_compare)

tup1 = zip(list_compare,all_files)

print(tup1)

tup2 = sorted(tup1, key=lambda x: (-x[0], x[1]))

print(tup2)


newpath = r"D:\python_workspaces\cv-man\new\\"

if not os.path.exists(newpath):
    os.makedirs(newpath)

increment = 0

for i,j in tup2:
    print(j)
    name = os.path.split(j)
    basename = name[1]
    #pathname = name[0]
    fn = "{}"
    increment += 1
    fn = fn.format(increment)
    target = str(newpath) + str(f"{fn}") + str("_") + str(basename)
    print(target)
    shutil.copyfile(j, target)











'''
files = [f for f in glob.glob("*.txt")]

for fi, f in enumerate(files):
    print(fi, f)

query = input("Please add your selection: ") # just the number
df = pd.read_csv(files[int(query)])
'''