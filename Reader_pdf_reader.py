# importing required modules 
from PyPDF2 import PdfReader 


def pdfReadModullar( filename,x):
    
# creating a pdf reader object 
    reader = PdfReader(filename) 

# printing number of pages in pdf file 
    print(len(reader.pages)) 
  
# getting a specific page from the pdf file 
    text = ""
    for i in range(x):
        page = reader.pages[i] 
        # extracting text from page 
        text = text + page.extract_text() 
    
    return text 

    