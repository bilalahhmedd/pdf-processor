import pandas as pd
import numpy as numpy
import PyPDF2 as pdf

# first of all initialize pdf object

def find_summary(doc_name):
    reader = pdf.PdfFileReader(open('example.pdf','rb'))
    text=''
    for i in range(reader.numPages):
        text= text+reader.getPage(i).extractText()
        # so we have text in our object
        # we can process it now
    if ('SUMMARY' in text):
        fnl = text[text.find('SUMMARY'):text.find('DATES')]
        fnl=fnl.replace('SUMMARY:','')
        fnl = fnl.replace('\n','') 
        fnl = fnl.replace('[','') 
        fnl = fnl.replace(']','') 
    else:
        fnl = 'Not found'
    return fnl