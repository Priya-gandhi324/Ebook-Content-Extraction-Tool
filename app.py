from flask import Flask, render_template, request
from pdf_parsers.pdf_reader_aspose import pdf2xml_aspose
from pdf_parsers.pdf_reader_plumber import pdf2text_pdfplumber
from pdf_parsers.pdf_reader_miner import pdf2html_pdfminer

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        pdf_link = request.form.get('content')
        converted_text = None
        
        if pdf_link:
            convert_to = request.form.get('convert_to')
            if convert_to == '1':
                converted_text = pdf2xml_aspose(pdf_link)
            elif convert_to == '2':
                converted_text = pdf2html_pdfminer(pdf_link)
            elif convert_to == '3':
                converted_text = pdf2text_pdfplumber(pdf_link)
            else:
                converted_text = 'Oops something went wrong! please try again'

            return render_template('index.html', converted_text=converted_text)

    return render_template('index.html')
 

if __name__ == "__main__": 
    app.run(debug=True)