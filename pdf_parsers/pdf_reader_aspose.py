import aspose.words as aw
import requests, os


def get_pdf_content(file_path, dir_name):
    doc = aw.Document(file_path)
    doc.save(os.path.join(dir_name, "pdf2xml.xml"))
    
    all_text = []
    
    with open(os.path.join(dir_name, 'pdf2xml.xml'), 'r', encoding='utf-8') as file:
        for line in file:
            all_text.append(line)
    
    return ''.join(all_text)


def pdf2xml_aspose(url):
    dir_name = f'local_files/'
    try:
        os.makedirs(dir_name)
    except Exception as e:
        pass

    file_path = dir_name + 'court.pdf'
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
    pdf_link = 'https://ncert.nic.in/textbook/pdf/gemh104.pdf'
    print(pdf2xml_aspose(pdf_link))