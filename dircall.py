import os
import logging
logging.basicConfig(filename ='logfile1.log',level='DEBUG',format='%(asctime)s-%(levelname)s-%(message)s')
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog


def get_dir():
    f=filedialog.askdirectory()
    merger=PdfFileMerger(strict=False)
    logging.info("User has entered directory {}".format(f))
    try:
        for i in os.listdir(f):
            if i.endswith('.pdf'):
                merger.append(i)
            else:
                pass
           
        merger.write("Merged_pdf.pdf")
        merger.close()
       
                
        logging.info("Directory exists in system and all pdf have been merged.Check your folder!!!")        
    
    except Exception as e:
        logging.error("Directory doesn't exists in system,check your path")
        logging.exception("Check your input:" + str(e))
        
window=Tk()
window.title("PDF Merger TK")
window.geometry("500x500")
button=Button(window,text='Click for file path')
button.config(command=get_dir)
button.pack()
window.mainloop()        