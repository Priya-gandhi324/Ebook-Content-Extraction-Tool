import pdfplumber, requests, os

def get_pdf_content(file_path):
    all_text = []
    with pdfplumber.open(file_path) as pdf:
        for i in range(len(pdf.pages)):
            text = pdf.pages[i].extract_text()
            all_text.append(text)
        return '\n'.join(all_text)


def pdf2text_pdfplumber(url):
    dir_name = f'local_files/'
    try:
        os.makedirs(dir_name)
    except Exception as e:
        pass
    file_path =  dir_name + 'court.pdf'
    for retry in range(3):
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.content:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                return get_pdf_content(file_path)
        except Exception as e:
            pass

if __name__ == "__main__":
    pdf_link = "https://ncert.nic.in/textbook/pdf/gemh104.pdf"
    print(pdf2text_pdfplumber(pdf_link))