# Requires Python 3.6 or higher due to f-strings

# Import libraries
import platform
from pathlib import Path
from tempfile import TemporaryDirectory

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re




if platform.system() == "Windows":
	# We may need to do some additional downloading and setup...
	# Windows needs a PyTesseract Download
	# https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine

	pytesseract.pytesseract.tesseract_cmd = (r"D:\\Tesseract-OCR\\tesseract.exe")
 
 
# Store all the pages of the PDF in a variable
 


	# Windows also needs poppler_exe
path_to_poppler_exe = Path(r"C:\\Program Files\\poppler-0.68.0\bin")
		

# Store all the pages of the PDF in a variable



def main(list_compare,find_word,PDF_file):

	image_file_list = []
	final_list = []
	''' Main execution point of the program'''

	# Create a temporary directory to hold our temporary images.

	"""
	Part #1 : Converting PDF to images
	"""

	if platform.system() == "Windows":
		pdf_pages = convert_from_path(
			PDF_file, 500, poppler_path=path_to_poppler_exe
		)
	else:
		pdf_pages = convert_from_path(PDF_file, 500)
	# Read in the PDF file at 500 DPI

	# Iterate through all the pages stored above
	for page_enumeration, page in enumerate(pdf_pages, start=1):
		# enumerate() "counts" the pages for us.
		filename = f"D:\python_workspaces\{page_enumeration}.jpg"

		# Declaring filename for each page of PDF as JPG
		# For each page, filename will be:
		# PDF page 1 -> page_001.jpg
		# PDF page 2 -> page_002.jpg
		# PDF page 3 -> page_003.jpg
		# ....
		# PDF page n -> page_00n.jpg

		# Save the image of the page in system
		page.save(filename, "JPEG")
		image_file_list.append(filename)
		print(image_file_list)

	"""
	Part #2 - Recognizing text from the images using OCR
	"""
	
		# Iterate from 1 to total number of pages
	for image_file in image_file_list:

		# Set filename to recognize text from
		# Again, these files will be:
		# page_1.jpg
		# page_2.jpg
		# ....
		# page_n.jpg

		# Recognize the text as string in image using pytesserct
		text = str(((pytesseract.image_to_string(Image.open(image_file)))))

		# The recognized text is stored in variable text
		# Any string processing may be applied on text
		# Here, basic formatting has been done:
		# In many PDFs, at line ending, if a word can't
		# be written fully, a 'hyphen' is added.
		# The rest of the word is written in the next line
		# Eg: This is a sample text this word here GeeksF-
		# orGeeks is half on first line, remaining on next.
		# To remove this, we replace every '-\n' to ''.
		text = text.replace("-\n", "")

		search = re.findall(fr'{find_word}',text)
		#search = re.findall(fr'\bis\b|\btest\b|\bor\b','This is a test string for the test')    

		final_list.append(len(search))
		
	list_compare.append(sum(final_list))
	print(list_compare)



				

				# Finally, write the processed text to the file.
				#output_file.write(text)

			# At the end of the with .. output_file block
			# the file is closed after writing all the text.
		# At the end of the with .. tempdir block, the
		# TemporaryDirectory() we're using gets removed!	
	# End of main function!
	
if __name__ == "__main__":
	# We only want to run this if it's directly executed!
	main()
