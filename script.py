from pdf_processor import find_summary
import os
root_dir = './'
import ntpath

# so now let's iterate through each directory
# get pdf file title
# extract summary
pdfs=[]
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.pdf'):
             pdfs.append(os.path.join(root, file))

# so we have paths of pdf files 
# let;s find summaries out of these files
summaries = []
for pdf in pdfs:
    summaries.append((ntpath.basename(pdf),find_summary(pdf)))
    print('doc processed succesfully')

# comment added to test
