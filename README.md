CV-MAN
--------

This is a python based program that filter the potential resumes/CVs by filtering them based on the amount of  mutiple given keywords they have, using OCR tesseract.

It first takes path as input where pdf files are stored and then read all Resumes/CVs in it, checking which one has the most highest amount of given targeted words in them.

Once the comparison is done, It create folder `/new/` in the same given path and list all pdf with numbers in their name where the one that has most amount of words in the top `1_file.pdf` and secondone in the second positions and so on.


----------------------------------------------------
Libraries used in this project 


pytesseract 0.3.10
`pip install pytesseract`


pdf2image 1.16.0
`pip install pdf2image`


Pillow 9.2.0
`pip install Pillow`

Libraries and their uses are covered by their respective licenses in [Libraries](https://github.com/saadk555/cv-man/tree/main/Libraries) directory 

----------------------------------------------------

Feel free to contribute and improve it. Any contribution would be highly appreciated.

----------------------------------------------------




