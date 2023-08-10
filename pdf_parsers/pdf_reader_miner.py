import os, requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from io import BytesIO
from pdfminer.layout import LAParams
from pdfminer.converter import HTMLConverter
from pdfminer.pdfpage import PDFPage


def get_pdf_content(content, dir_name):
    resource_manager = PDFResourceManager(caching=True)
    outtxt = BytesIO()
    la = LAParams(word_margin=0)
    text_converter = HTMLConverter(resource_manager, outtxt, laparams=la)
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    
    if content:
        file = open(content, 'rb')
    
    for page in PDFPage.get_pages(file, pagenos=set(), maxpages=0, password='', caching=True, check_extractable=True):
        interpreter.process_page(page)
    
    text = outtxt.getvalue()
    file.close()
    text_converter.close()
    outtxt.close()
    
    with open(dir_name + 'orissa_hc.html', 'wb') as file:
        file.write(text)
    
    return text.decode()


def pdf2html_pdfminer(url):
    dir_name = f'local_files/'
    try:
        os.makedirs(dir_name)
    except Exception as e:
        pass

    file_path = dir_name + 'orissa_hc.pdf'
    for retry in range(3):
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.content:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                return get_pdf_content(file_path, dir_name)
        except Exception as e:
            pass

if __name__ == "__main__":
    pdf_link = 'https://storage.googleapis.com/legistify-dev-public/prod/litigation/causelist_docs/pdf/orissa_highcourt/30-01-2023_Weekly-List.pdf'
    pdf2html_pdfminer(pdf_link)